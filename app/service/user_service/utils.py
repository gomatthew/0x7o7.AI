# -*- coding: utf-8 -*-
import hashlib
from typing import Union
from jose import jwt
from datetime import timedelta, datetime
from passlib.context import CryptContext
from app import app

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_salt(phone: str, row_password: str):
    hash_str = phone + row_password
    hash_str_encode = hash_str.encode('UTF-8')
    return hashlib.md5(hash_str_encode).hexdigest()


def get_password_hash(row_password: str, salt: str):
    return pwd_context.hash(row_password + salt)


def verify_password(row_password: str, hashed_password: str):
    return pwd_context.verify(row_password, hashed_password)


def decode_access_token(token) -> Union[str, None]:
    try:
        payload = jwt.decode(token, app.config.get('SECRET_KEY'), algorithms=[app.config.get('ALGORITHM')])
        user_id = payload.get('data').get('user_id')
        return user_id
    except BaseException:
        return None


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=1440)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, app.config.get('SECRET_KEY'), algorithm=app.config.get('ALGORITHM'))
    return encoded_jwt
