"""
Service cô lập cho Facebook OAuth2 – US-ACC-004.

Chịu trách nhiệm:
  1. Tạo URL chuyển hướng tới Facebook Login Dialog.
  2. Đổi authorization code lấy access_token.
  3. Gọi Graph API /me lấy thông tin người dùng.

Không chứa logic tạo User / JWT – phần đó nằm trong router.
"""

import json
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from app.core.config import settings

# ── Hằng số Facebook OAuth ────────────────────────────────────
FACEBOOK_AUTH_URL = "https://www.facebook.com/v19.0/dialog/oauth"
FACEBOOK_TOKEN_URL = "https://graph.facebook.com/v19.0/oauth/access_token"
FACEBOOK_USER_INFO_URL = "https://graph.facebook.com/v19.0/me"

class FacebookAuthError(Exception):
    """Lỗi khi giao tiếp với Facebook API."""

    def __init__(self, message: str = "Không thể xác thực với Facebook"):
        self.message = message
        super().__init__(self.message)


def _get_json(url: str, params: dict[str, str]) -> dict:
        request = Request(f"{url}?{urlencode(params)}")
        try:
            with urlopen(request, timeout=10) as response:
                if response.status != 200:
                    raise FacebookAuthError("Facebook API trả về lỗi")
                try:
                    data = json.loads(response.read())
                except (UnicodeDecodeError, ValueError):
                    raise FacebookAuthError("Facebook trả về phản hồi không hợp lệ")
        except HTTPError:
            raise FacebookAuthError("Facebook API trả về lỗi")
        except (TimeoutError, URLError):
            raise FacebookAuthError("Không thể kết nối tới Facebook, vui lòng thử lại sau")

        if not isinstance(data, dict):
            raise FacebookAuthError("Facebook trả về phản hồi không hợp lệ")
        return data


# ── Public helpers ─────────────────────────────────────────────

def get_facebook_auth_url() -> str:
    """Trả về URL đầy đủ để redirect trình duyệt tới Facebook Login Dialog."""
    params = {
        "client_id": settings.facebook_client_id,
        "redirect_uri": settings.facebook_redirect_uri,
        "scope": "public_profile,email",
        "response_type": "code",
    }
    return f"{FACEBOOK_AUTH_URL}?{urlencode(params)}"


def exchange_code_for_token(code: str) -> str:
    """Đổi authorization *code* lấy access_token từ Facebook.

    Returns:
        access_token (str)

    Raises:
        FacebookAuthError – nếu Facebook từ chối hoặc timeout.
    """
    params = {
        "client_id": settings.facebook_client_id,
        "client_secret": settings.facebook_client_secret,
        "redirect_uri": settings.facebook_redirect_uri,
        "code": code,
    }
    data = _get_json(FACEBOOK_TOKEN_URL, params)
    access_token = data.get("access_token")
    if not isinstance(access_token, str) or not access_token:
        raise FacebookAuthError("Mã xác thực Facebook không hợp lệ hoặc đã hết hạn")

    return access_token


def get_facebook_user_info(access_token: str) -> dict:
    """Gọi Graph API ``/me`` lấy thông tin người dùng.

    Returns:
        dict với ít nhất ``id`` và ``name``; ``email`` có thể thiếu.

    Raises:
        FacebookAuthError – nếu token không hợp lệ hoặc lỗi mạng.
    """
    params = {
        "fields": "id,name,email",
        "access_token": access_token,
    }
    data = _get_json(FACEBOOK_USER_INFO_URL, params)
    provider_id = data.get("id")
    if not isinstance(provider_id, (str, int)) or not str(provider_id).strip():
        raise FacebookAuthError("Không lấy được thông tin người dùng từ Facebook")
    data["id"] = str(provider_id)

    return data
