# -*- coding: utf-8 -*-
import traceback
from .utils import *
from app import app
from app.utils import dt
from app.dto import BaseResponse, UserDTO
from app.controller import user_router as router
from app.liberary.db.repository.user_repository import add_user_to_db, update_user_token


@router.post('/add', response_model=BaseResponse)
def add_user(user_info: UserDTO):
    try:
        app.logger.info('🟢 Add user start.')
        user_name = user_info.get('username')
        user_email = user_info.get('email')
        user_phone = user_info.get('phone')
        user_password = user_info.get('password')
        salt = get_salt(phone=user_phone, row_password=user_password)
        hashed_password = get_password_hash(user_password, salt)
        user_id = add_user_to_db(username=user_name, email=user_email, password=hashed_password, phone=user_phone,
                                 salt=salt, token=None)
        token_payload = {'iat': dt.now, 'iss': '0x7o7_AI', 'data': {'user_id': user_id}}
        token = create_access_token(token_payload)
        update_user_token(user_id, token)
        app.logger.info('🟢 Add user Finish.')
        return BaseResponse(status=200, message='add user success.', data={'token': token})
    except BaseException as e:
        app.logger.error('🔴 Add user Error.')
        app.logger.error(traceback.format_exc())
        app.logger.error(e)
        return BaseResponse(statistics=500, message='Server Error')
