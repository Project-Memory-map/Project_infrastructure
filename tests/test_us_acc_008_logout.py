"""Backend API tests for US-ACC-008 logout and session validation."""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import BigInteger, create_engine, event
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.database import Base, get_db
from app.core.security import create_access_token
from app.main import app
from app.modules.accounts.models import User


@compiles(BigInteger, "sqlite")
def _compile_bigint_for_sqlite(type_, compiler, **kwargs):
    return compiler.visit_INTEGER(type_, **kwargs)


engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)


@event.listens_for(engine, "connect")
def _enable_sqlite_foreign_keys(connection, _record):
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


TestSession = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def override_get_db():
    db = TestSession()
    try:
        yield db
    finally:
        db.close()


client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_database():
    previous_override = app.dependency_overrides.get(get_db)
    app.dependency_overrides[get_db] = override_get_db
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
    if previous_override is None:
        app.dependency_overrides.pop(get_db, None)
    else:
        app.dependency_overrides[get_db] = previous_override


def _create_user():
    with TestSession() as db:
        user = User(
            email="logout@example.com",
            password_hash=None,
            display_name="Logout User",
            role="user",
            status="active",
            token_version=0,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user.id


def _auth_headers(user_id: int, token_version: int = 0):
    token = create_access_token(user_id, "user", token_version)
    return {"Authorization": f"Bearer {token}"}


def _assert_no_cache(response):
    assert response.headers["cache-control"] == "no-store, no-cache, must-revalidate, max-age=0"
    assert response.headers["pragma"] == "no-cache"
    assert response.headers["expires"] == "0"


def test_logout_requires_valid_token_and_returns_no_cache_json():
    user_id = _create_user()

    response = client.post("/api/auth/logout", headers=_auth_headers(user_id))

    assert response.status_code == 200
    assert response.json()["message"] == "Đăng xuất thành công"
    _assert_no_cache(response)


@pytest.mark.parametrize("path,method", [
    ("/api/auth/logout", "post"),
    ("/api/auth/me", "get"),
])
def test_private_auth_endpoints_reject_missing_token(path, method):
    response = getattr(client, method)(path)

    assert response.status_code == 401
    assert "đăng nhập" in response.json()["message"].lower()
    _assert_no_cache(response)


def test_private_auth_endpoint_rejects_token_with_old_version():
    user_id = _create_user()
    old_token_headers = _auth_headers(user_id, token_version=0)

    with TestSession() as db:
        user = db.get(User, user_id)
        user.token_version += 1
        db.commit()

    response = client.get("/api/auth/me", headers=old_token_headers)

    assert response.status_code == 401
    assert "phiên đăng nhập không còn hiệu lực" in response.json()["message"].lower()
    assert response.json()["data"] is None
    _assert_no_cache(response)
