from datetime import datetime, timezone

from fastapi import APIRouter, Depends, Query, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.errors import AppException, ForbiddenException
from app.core.response import build_response
from app.core.security import create_access_token
from app.modules.accounts.deps import get_current_user
from app.modules.accounts.models import OAuthAccount, User
from app.modules.accounts.schemas import UserResponse
from app.modules.accounts.services.facebook_auth import (
    FacebookAuthError,
    exchange_code_for_token,
    get_facebook_auth_url,
    get_facebook_user_info,
)

router = APIRouter(prefix="/api/auth", tags=["M1 - Tài khoản"])


@router.get("/me")
def read_me(request: Request, current_user: User = Depends(get_current_user)):
    data = UserResponse.model_validate(current_user)
    return build_response(200, "Lấy thông tin tài khoản thành công", request, data=data)


@router.post("/logout", summary="Đăng xuất khỏi hệ thống", dependencies=[Depends(get_current_user)])
def logout(request: Request):
    return build_response(200, "Đăng xuất thành công", request)


# ── US-ACC-004: Đăng nhập bằng Facebook ───────────────────────


@router.get("/facebook", summary="Redirect tới Facebook Login Dialog")
def facebook_login():
    """Chuyển hướng trình duyệt tới trang đăng nhập Facebook."""
    return RedirectResponse(url=get_facebook_auth_url())


@router.get("/facebook/callback", summary="Facebook OAuth callback")
def facebook_callback(
    request: Request,
    code: str | None = Query(default=None),
    error: str | None = Query(default=None),
    db: Session = Depends(get_db),
):
    """Xử lý callback từ Facebook sau khi người dùng đồng ý/hủy cấp quyền.

    Acceptance Criteria xử lý:
      - AC1: Đăng nhập lần đầu → tạo user mới.
      - AC2: Facebook không trả email → user.email = NULL, missing_email = true.
      - AC3: Người dùng hủy → quay lại trang đăng nhập với thông báo rõ ràng.
      - Email Facebook chưa xác minh không được dùng để liên kết tài khoản.
      - Cross-Story #2: Tài khoản bị khóa → HTTP 403.
    """

    # ── AC3: Người dùng hủy trên màn hình Facebook ───────────
    if error or not code:
        raise AppException("Đăng nhập Facebook chưa hoàn tất")

    # ── Đổi code lấy access_token & thông tin người dùng ─────
    try:
        access_token = exchange_code_for_token(code)
        fb_user = get_facebook_user_info(access_token)
    except FacebookAuthError as exc:
        raise AppException(exc.message)

    fb_id = str(fb_user["id"]).strip()
    fb_name = fb_user.get("name")
    if not isinstance(fb_name, str) or not fb_name.strip():
        fb_name = "Người dùng Facebook"
    fb_email = fb_user.get("email")
    if isinstance(fb_email, str):
        fb_email = fb_email.strip().lower() or None
    else:
        fb_email = None

    # ── Tìm user hiện có qua oauth_accounts (facebook_id) ────
    oauth_row = (
        db.query(OAuthAccount)
        .filter(OAuthAccount.provider == "facebook", OAuthAccount.provider_user_id == fb_id)
        .first()
    )

    user: User | None = None

    if oauth_row:
        # Đã liên kết trước đó → lấy user hiện có
        user = db.get(User, oauth_row.user_id)
    else:
        # Facebook does not establish email ownership, so never link by email.
        if fb_email and db.query(User.id).filter(User.email == fb_email).first():
            fb_email = None

        # ── AC1 + AC2: Tạo tài khoản mới ────────────────────────
        user = User(
            email=fb_email,
            password_hash=None,
            display_name=fb_name,
            role="user",
            status="active",
        )
        db.add(user)
        db.flush()

        db.add(OAuthAccount(user_id=user.id, provider="facebook", provider_user_id=fb_id))
        db.flush()

    # ── Cross-Story #2: Tài khoản bị khóa ────────────────────
    if user.status == "locked":
        db.rollback()
        raise ForbiddenException("Tài khoản của bạn đã bị khóa")

    # ── Cập nhật last_login_at ────────────────────────────────
    user.last_login_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(user)

    # ── Cấp JWT (Cross-Story #4) ─────────────────────────────
    jwt_token = create_access_token(user.id, user.role, user.token_version)

    response_data = {
        "access_token": jwt_token,
        "token_type": "bearer",
        "user": UserResponse.model_validate(user).model_dump(),
    }
    if not user.email:
        response_data["missing_email"] = True
        return build_response(
            200,
            "Vui lòng bổ sung email trong hồ sơ để dùng chức năng quên mật khẩu",
            request,
            data=response_data,
        )

    return build_response(200, "Đăng nhập thành công", request, data=response_data)
