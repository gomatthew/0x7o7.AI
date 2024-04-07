# -*- coding: utf-8 -*-
import traceback
from .utils import *
from app import app
from app.utils import dt
from app.dto import BaseResponse, UserDTO
from app.routers.router import user_router as router
from app.liberary.db.repository.user_repository import add_user_to_db, update_user_token


@router.post('/add', response_model=BaseResponse)
async def add_user(user_info: UserDTO):
    try:
        app.logger.info('🟢 Add user start.')
        user_name = user_info.username
        user_email = user_info.email
        user_phone = user_info.phone
        user_password = user_info.password
        if not user_name or not user_email or not user_phone or not user_password:
            return BaseResponse(status=200, message="用户名-邮箱-手机号-密码 均不可为空")
        salt = get_salt(phone=user_phone, row_password=user_password)
        hashed_password = get_password_hash(user_password, salt)
        user_id = add_user_to_db(username=user_name, email=user_email, password=hashed_password, phone=user_phone,
                                 salt=salt, token=None, create_user='0x7o7')
        if not user_id:
            return BaseResponse(status=200, message="用户已存在")
        token_payload = {'iat': dt.now, 'iss': '0x7o7_AI', 'data': {'user_id': user_id}}
        token = create_access_token(token_payload)
        update_user_token(user_id, token)
        app.logger.info(f'🟢 Add user :{user_id} Finish.')
        return BaseResponse(status=200, message='add user success.', data={'token': token})
    except BaseException as e:
        app.logger.error('🔴 Add user Error.')
        app.logger.error(traceback.format_exc())
        app.logger.error(e)
        return BaseResponse(status=500, message='Server Error')
