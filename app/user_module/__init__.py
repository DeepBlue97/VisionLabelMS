from fastapi import APIRouter

from app.user_module.service import ()
from app.user_module.schemas import ()


user_router = APIRouter()

user_router.add_api_route(path="/role/all",
                          endpoint="get_role_all",
                          response_model=RoleListResponse,
                          summary="获取所有角色",
                          methods=["GET"])

