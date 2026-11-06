from fastapi import APIRouter, Depends, Request

from app.core.response import build_response
from app.modules.accounts.deps import get_current_user
from app.modules.accounts.models import User
from app.modules.accounts.schemas import UserResponse

router = APIRouter(prefix="/api/auth", tags=["M1 - Tài khoản"])


@router.get("/me")
def read_me(request: Request, current_user: User = Depends(get_current_user)):
    data = UserResponse.model_validate(current_user)
    return build_response(200, "Lấy thông tin tài khoản thành công", request, data=data)
