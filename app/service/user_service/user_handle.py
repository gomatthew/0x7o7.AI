# -*- coding: utf-8 -*-
from app.dto.user_dto import UserDTO
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


def add_user(user_info: UserDTO):
    user_name = user_info.get('username')
    user_email = user_info.get('email')
    user_phone = user_info.get('email')
    user_passwor = user_info.get('email')
    # 1 .生成salt 2. 生成token


from typing import Annotated


def process_data(data: Annotated[str, "user input"]) -> None:
    print("Received data:", data)


process_data("Hello")
