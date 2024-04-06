# -*- coding: utf-8 -*-
import traceback

from fastapi import Request

from app import app
from app.utils import dt
from app.controller.router import user_router as router
from app.dto import UserLoginDTO, BaseResponse
from app.liberary.db.repository.user_repository import update_user_token, user_checkin
from .utils import verify_password, create_access_token, decode_access_token


@router.post('/login', response_model=BaseResponse)
async def user_login(user_info: UserLoginDTO):
    try:
        user_account = user_info.account
        row_password = user_info.password
        app.logger.info(f'🟢 User : {user_account} login Start.')
        user_id, salt, hash_password = user_checkin(user_account)
        if not user_id:
            return BaseResponse(status=200, message='未注册账户')
        verify_result = verify_password(row_password + salt, hash_password)
        if verify_result:
            token_payload = {'iat': dt.now, 'iss': '0x7o7_AI', 'data': {'user_id': user_id}}
            token = create_access_token(token_payload)
            update_user_token(user_id, token)
            app.logger.info('🟢 User login success.')
            return BaseResponse(status=200, message='success', data={'token': token})
        else:
            app.logger.info('🟢 User login fail with wrong password or account.')
            return BaseResponse(status=200, message='用户名或密码错误')

    except BaseException as e:
        app.logger.error('🔴 User login error.')
        app.logger.error(traceback.format_exc())
        app.logger.error(e)
        return BaseResponse(status=500, message='Server error.')


def auth_checkin(request: Request):
    headers = request.headers
    token = headers.get('token')
    user_id = decode_access_token(token)
    if user_id:
        return BaseResponse(status=200, message='token auth success', dataclasses={'user_id': user_id})
    else:
        return BaseResponse(status=401, message='token auth failed')
