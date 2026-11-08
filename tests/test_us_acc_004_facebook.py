"""
Unit Tests cho US-ACC-004 – Đăng nhập bằng Facebook.

Kiểm tra đầy đủ 3 Acceptance Criteria + edge cases liên module:
  - AC1: Đăng nhập Facebook lần đầu → tạo tài khoản mới.
  - AC2: Facebook không cung cấp email → user.email = NULL, missing_email = true.
  - AC3: Người dùng hủy → quay lại trang đăng nhập với thông báo.
  - Edge: Email Facebook chưa xác minh không liên kết tài khoản hiện hữu.
  - Edge: Tài khoản bị khóa → HTTP 403.
  - Edge: Token Facebook không hợp lệ → HTTP 400.
  - Edge: Đăng nhập lại (đã có facebook_id) → đăng nhập bình thường.

Sử dụng unittest.mock để patch các hàm gọi Facebook API,
KHÔNG gọi thật ra internet.
"""

from unittest.mock import patch

import pytest
from sqlalchemy import BigInteger, Enum as SAEnum, create_engine, event
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

# ── SQLite compatibility patches (PHẢI TRƯỚC import models) ────

# 1) BigInteger → INTEGER cho SQLite (AUTOINCREMENT cần INTEGER PK)
@compiles(BigInteger, "sqlite")
def _bi_sqlite(element, compiler, **kw):
    return "INTEGER"

# 2) Enum → non-native cho SQLite (không hỗ trợ ENUM type)
_orig_enum_init = SAEnum.__init__
def _patched_enum_init(self, *args, **kwargs):
    kwargs.setdefault("native_enum", False)
    _orig_enum_init(self, *args, **kwargs)
SAEnum.__init__ = _patched_enum_init

# ── Bây giờ mới import app modules ────────────────────────────
from fastapi.testclient import TestClient  # noqa: E402

from app.core.database import Base, get_db  # noqa: E402
from app.main import app  # noqa: E402
from app.modules.accounts.models import OAuthAccount, User  # noqa: E402
from app.modules.accounts.services.facebook_auth import FacebookAuthError  # noqa: E402

# ── Test DB (SQLite in-memory) ─────────────────────────────────
engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)


@event.listens_for(engine, "connect")
def _set_sqlite_pragma(dbapi_conn, connection_record):
    cursor = dbapi_conn.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


TestingSession = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def override_get_db():
    db = TestingSession()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app, follow_redirects=False)

# ── Patch the symbols used by the router ────────────────────────
_SVC = "app.modules.accounts.router"

# Dữ liệu mẫu Facebook
FB_USER_FULL = {"id": "10001", "name": "Nguyễn Văn A", "email": "nguyenvana@gmail.com"}
FB_USER_NO_EMAIL = {"id": "10002", "name": "Trần Thị B"}
FB_ACCESS_TOKEN = "EAAGm0PX4ZCps..."


# ── Fixtures ───────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def setup_db():
    """Tạo bảng trước mỗi test và xóa sau khi test xong."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def db_session():
    db = TestingSession()
    try:
        yield db
    finally:
        db.close()


def _create_user(db: Session, **overrides) -> User:
    """Helper tạo user trong DB test."""
    defaults = {
        "email": None,
        "password_hash": None,
        "display_name": "Test User",
        "role": "user",
        "status": "active",
        "token_version": 0,
        "failed_login_count": 0,
    }
    defaults.update(overrides)
    user = User(**defaults)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def _create_oauth(db: Session, user_id: int, provider: str, provider_user_id: str) -> OAuthAccount:
    """Helper tạo oauth_account trong DB test."""
    oauth = OAuthAccount(user_id=user_id, provider=provider, provider_user_id=provider_user_id)
    db.add(oauth)
    db.commit()
    db.refresh(oauth)
    return oauth


def _login_data(response):
    assert response.status_code == 200
    return response.json()["data"]


# ══════════════════════════════════════════════════════════════
#  AC1 – Đăng nhập Facebook lần đầu
# ══════════════════════════════════════════════════════════════

class TestAC1_FirstLogin:
    """Đăng nhập Facebook lần đầu: tạo tài khoản mới, role=user, cấp JWT."""

    @patch(f"{_SVC}.get_facebook_user_info", return_value=FB_USER_FULL)
    @patch(f"{_SVC}.exchange_code_for_token", return_value=FB_ACCESS_TOKEN)
    def test_first_login_creates_user_and_returns_jwt(self, mock_exchange, mock_info, db_session):
        resp = client.get("/api/auth/facebook/callback", params={"code": "valid_code"})

        body = resp.json()
        assert body["message"] == "Đăng nhập thành công"
        data = _login_data(resp)
        assert data["access_token"]
        assert data["token_type"] == "bearer"
        assert data["user"]["display_name"] == "Nguyễn Văn A"
        assert data["user"]["email"] == "nguyenvana@gmail.com"
        mock_exchange.assert_called_once_with("valid_code")
        mock_info.assert_called_once_with(FB_ACCESS_TOKEN)

        # Kiểm tra user trong DB
        user = db_session.query(User).filter(User.email == "nguyenvana@gmail.com").first()
        assert user is not None
        assert user.display_name == "Nguyễn Văn A"
        assert user.role == "user"
        assert user.password_hash is None  # Cross-Story #3

        # Kiểm tra oauth_accounts
        oauth = (
            db_session.query(OAuthAccount)
            .filter(OAuthAccount.provider == "facebook", OAuthAccount.provider_user_id == "10001")
            .first()
        )
        assert oauth is not None
        assert oauth.user_id == user.id

    @patch(f"{_SVC}.get_facebook_user_info", return_value=FB_USER_FULL)
    @patch(f"{_SVC}.exchange_code_for_token", return_value=FB_ACCESS_TOKEN)
    def test_jwt_contains_required_claims(self, mock_exchange, mock_info):
        """JWT phải chứa user_id, role, token_version (Cross-Story #4)."""
        from app.core.security import decode_access_token

        resp = client.get("/api/auth/facebook/callback", params={"code": "valid_code"})
        token = _login_data(resp)["access_token"]
        payload = decode_access_token(token)

        assert payload is not None
        assert "sub" in payload       # user_id
        assert "role" in payload
        assert payload["role"] == "user"
        assert "tv" in payload        # token_version


# ══════════════════════════════════════════════════════════════
#  AC2 – Facebook không cung cấp email
# ══════════════════════════════════════════════════════════════

class TestAC2_MissingEmail:
    """Facebook không trả email → user.email = NULL, response kèm missing_email."""

    @patch(f"{_SVC}.get_facebook_user_info", return_value=FB_USER_NO_EMAIL)
    @patch(f"{_SVC}.exchange_code_for_token", return_value=FB_ACCESS_TOKEN)
    def test_no_email_creates_user_with_null_email(self, mock_exchange, mock_info, db_session):
        resp = client.get("/api/auth/facebook/callback", params={"code": "valid_code"})

        body = resp.json()
        data = _login_data(resp)
        assert data["missing_email"] is True
        assert "bổ sung email" in body["message"].lower()
        assert data["user"]["email"] is None

        # DB check
        user = db_session.query(User).filter(User.display_name == "Trần Thị B").first()
        assert user is not None
        assert user.email is None
        assert user.password_hash is None

    @patch(f"{_SVC}.get_facebook_user_info", return_value=FB_USER_NO_EMAIL)
    @patch(f"{_SVC}.exchange_code_for_token", return_value=FB_ACCESS_TOKEN)
    def test_no_email_message_reminds_user(self, mock_exchange, mock_info):
        resp = client.get("/api/auth/facebook/callback", params={"code": "valid_code"})
        assert "bổ sung email" in resp.json()["message"].lower()


# ══════════════════════════════════════════════════════════════
#  AC3 – Người dùng hủy trên Facebook
# ══════════════════════════════════════════════════════════════

class TestAC3_UserCancelled:
    """Người dùng hủy → quay lại đăng nhập với thông báo rõ ràng."""

    def test_cancel_with_error_param(self):
        resp = client.get(
            "/api/auth/facebook/callback",
            params={"error": "access_denied", "error_reason": "user_denied"},
        )
        assert resp.status_code == 400
        assert resp.json()["message"] == "Đăng nhập Facebook chưa hoàn tất"

    def test_cancel_without_code(self):
        resp = client.get("/api/auth/facebook/callback")
        assert resp.status_code == 400
        assert resp.json()["message"] == "Đăng nhập Facebook chưa hoàn tất"

    def test_cancel_with_error_and_code_still_rejects(self):
        """Nếu cả error lẫn code đều có, error ưu tiên."""
        resp = client.get(
            "/api/auth/facebook/callback",
            params={"error": "access_denied", "code": "some_code"},
        )
        assert resp.status_code == 400
        assert resp.json()["message"] == "Đăng nhập Facebook chưa hoàn tất"


# ══════════════════════════════════════════════════════════════
#  Edge case: Email trùng chưa xác minh không được liên kết
# ══════════════════════════════════════════════════════════════

class TestUnverifiedEmailCollision:
    """Email Facebook không xác minh quyền sở hữu; tài khoản hiện hữu không bị liên kết."""

    @patch(f"{_SVC}.get_facebook_user_info", return_value=FB_USER_FULL)
    @patch(f"{_SVC}.exchange_code_for_token", return_value=FB_ACCESS_TOKEN)
    def test_existing_email_does_not_link_facebook(self, mock_exchange, mock_info, db_session):
        # Tạo user đã đăng ký bằng email (register thường)
        existing = _create_user(
            db_session,
            email="nguyenvana@gmail.com",
            password_hash="$2b$12$hashedpassword",
            display_name="Anh A",
        )
        original_id = existing.id

        resp = client.get("/api/auth/facebook/callback", params={"code": "valid_code"})

        data = _login_data(resp)
        assert data["missing_email"] is True

        # Facebook identity is separate and the existing user is unchanged.
        assert db_session.query(User).count() == 2
        db_session.refresh(existing)
        assert existing.display_name == "Anh A"
        assert existing.password_hash == "$2b$12$hashedpassword"
        assert db_session.query(User).filter(User.id != original_id, User.email.is_(None)).count() == 1
        oauth = (
            db_session.query(OAuthAccount)
            .filter(OAuthAccount.user_id != original_id, OAuthAccount.provider == "facebook")
            .first()
        )
        assert oauth is not None
        assert oauth.user_id != original_id

    @patch(f"{_SVC}.get_facebook_user_info", return_value={**FB_USER_FULL, "email": "NGUYENVANA@Gmail.COM"})
    @patch(f"{_SVC}.exchange_code_for_token", return_value=FB_ACCESS_TOKEN)
    def test_email_case_insensitive_matching(self, mock_exchange, mock_info, db_session):
        """Email chuẩn hóa trước khi kiểm tra collision, nhưng không liên kết."""
        existing = _create_user(db_session, email="nguyenvana@gmail.com", display_name="Anh A")

        resp = client.get("/api/auth/facebook/callback", params={"code": "valid_code"})
        assert _login_data(resp)["missing_email"] is True
        assert db_session.query(User).count() == 2
        db_session.refresh(existing)
        assert existing.email == "nguyenvana@gmail.com"
        assert db_session.query(User).filter(User.email.is_(None)).count() == 1


# ══════════════════════════════════════════════════════════════
#  Edge case: Tài khoản bị khóa
# ══════════════════════════════════════════════════════════════

class TestCrossStory_LockedAccount:
    """Cross-Story #2: Tài khoản bị khóa → HTTP 403."""

    @patch(f"{_SVC}.get_facebook_user_info", return_value=FB_USER_FULL)
    @patch(f"{_SVC}.exchange_code_for_token", return_value=FB_ACCESS_TOKEN)
    def test_locked_account_returns_403(self, mock_exchange, mock_info, db_session):
        locked_user = _create_user(
            db_session,
            email="nguyenvana@gmail.com",
            display_name="Locked User",
            status="locked",
        )
        _create_oauth(db_session, locked_user.id, "facebook", "10001")

        resp = client.get("/api/auth/facebook/callback", params={"code": "valid_code"})
        assert resp.status_code == 403
        assert "bị khóa" in resp.json()["message"]

    @patch(f"{_SVC}.get_facebook_user_info", return_value=FB_USER_FULL)
    @patch(f"{_SVC}.exchange_code_for_token", return_value=FB_ACCESS_TOKEN)
    def test_matching_unverified_email_does_not_log_into_locked_account(self, mock_exchange, mock_info, db_session):
        """Email trùng không xác minh không thể liên kết hoặc đăng nhập user bị khóa."""
        locked_user = _create_user(
            db_session,
            email="nguyenvana@gmail.com",
            display_name="Locked Email User",
            status="locked",
        )

        resp = client.get("/api/auth/facebook/callback", params={"code": "valid_code"})
        assert _login_data(resp)["missing_email"] is True
        db_session.refresh(locked_user)
        assert locked_user.status == "locked"
        assert db_session.query(User).count() == 2
        assert db_session.query(OAuthAccount).filter(OAuthAccount.user_id == locked_user.id).count() == 0


# ══════════════════════════════════════════════════════════════
#  Edge case: Token/code Facebook không hợp lệ
# ══════════════════════════════════════════════════════════════

class TestEdge_InvalidFacebookToken:
    """Facebook API lỗi → HTTP 400, không văng 500."""

    @patch(f"{_SVC}.exchange_code_for_token", side_effect=FacebookAuthError("Mã xác thực Facebook không hợp lệ hoặc đã hết hạn"))
    def test_invalid_code_returns_400(self, mock_exchange):
        resp = client.get("/api/auth/facebook/callback", params={"code": "invalid_code"})
        assert resp.status_code == 400
        assert "không hợp lệ" in resp.json()["message"]

    @patch(f"{_SVC}.exchange_code_for_token", side_effect=FacebookAuthError("Facebook không phản hồi, vui lòng thử lại sau"))
    def test_facebook_timeout_returns_400(self, mock_exchange):
        resp = client.get("/api/auth/facebook/callback", params={"code": "code"})
        assert resp.status_code == 400
        assert "thử lại" in resp.json()["message"]

    @patch(f"{_SVC}.get_facebook_user_info", side_effect=FacebookAuthError("Token Facebook không hợp lệ"))
    @patch(f"{_SVC}.exchange_code_for_token", return_value=FB_ACCESS_TOKEN)
    def test_invalid_access_token_returns_400(self, mock_exchange, mock_info):
        resp = client.get("/api/auth/facebook/callback", params={"code": "code"})
        assert resp.status_code == 400


# ══════════════════════════════════════════════════════════════
#  Edge case: Đăng nhập lại (đã có facebook_id)
# ══════════════════════════════════════════════════════════════

class TestEdge_ReturningUser:
    """User đã liên kết facebook_id → đăng nhập lại bình thường."""

    @patch(f"{_SVC}.get_facebook_user_info", return_value=FB_USER_FULL)
    @patch(f"{_SVC}.exchange_code_for_token", return_value=FB_ACCESS_TOKEN)
    def test_returning_user_gets_jwt(self, mock_exchange, mock_info, db_session):
        user = _create_user(db_session, email="nguyenvana@gmail.com", display_name="Anh A")
        _create_oauth(db_session, user.id, "facebook", "10001")

        resp = client.get("/api/auth/facebook/callback", params={"code": "valid_code"})
        data = _login_data(resp)
        assert "access_token" in data
        assert "missing_email" not in data  # user already has an email

    @patch(f"{_SVC}.get_facebook_user_info", return_value=FB_USER_NO_EMAIL)
    @patch(f"{_SVC}.exchange_code_for_token", return_value=FB_ACCESS_TOKEN)
    def test_returning_user_without_email_still_gets_flag(self, mock_exchange, mock_info, db_session):
        user = _create_user(db_session, display_name="No Email User")
        _create_oauth(db_session, user.id, "facebook", "10002")

        resp = client.get("/api/auth/facebook/callback", params={"code": "valid_code"})
        assert _login_data(resp)["missing_email"] is True


# ══════════════════════════════════════════════════════════════
#  Edge case: Redirect endpoint
# ══════════════════════════════════════════════════════════════

class TestRedirectEndpoint:
    """GET /api/auth/facebook phải trả về redirect 307 tới Facebook."""

    def test_redirect_to_facebook(self):
        resp = client.get("/api/auth/facebook")
        assert resp.status_code == 307
        location = resp.headers.get("location", "")
        assert "facebook.com" in location
        assert "client_id" in location


class TestFacebookServiceResponses:
    """Malformed provider responses must become client-facing auth errors."""

    @patch("app.modules.accounts.services.facebook_auth.urlopen")
    def test_malformed_token_response_raises_auth_error(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.status = 200
        mock_urlopen.return_value.__enter__.return_value.read.return_value = b"invalid JSON"

        from app.modules.accounts.services.facebook_auth import exchange_code_for_token

        with pytest.raises(FacebookAuthError, match="phản hồi không hợp lệ"):
            exchange_code_for_token("code")

    @patch("app.modules.accounts.services.facebook_auth.urlopen")
    def test_malformed_profile_response_raises_auth_error(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.status = 200
        mock_urlopen.return_value.__enter__.return_value.read.return_value = b"[]"

        from app.modules.accounts.services.facebook_auth import get_facebook_user_info

        with pytest.raises(FacebookAuthError, match="phản hồi không hợp lệ"):
            get_facebook_user_info("token")
