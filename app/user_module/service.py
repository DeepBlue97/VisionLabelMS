
from pydantic import BaseModel

from app.user_module.schemas import User
# 查询用户


async def del_role(request: Request, 
                   role_id: int = Query(..., title="角色ID", ge=1)):
    """
    删除角色
    """
    
    user_cookie = request.cookies.get("user_cookie")


    return {"role_id": role_id}

    
async def login(response: Response,
                user: UserLogin = Depends(info_set_password)):

    return {"msg": "登录成功"}

async def logout():

    return {"msg": "退出成功"}


async def registe():
    return {"msg": "注册成功"}

