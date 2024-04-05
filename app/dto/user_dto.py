# -*- coding: utf-8 -*-
from pydantic import BaseModel, Field


class TokenDTO(BaseModel):
    access_token: str
    token_type: str


class UserDTO(BaseModel):
    username: str
    email: str
    phone: str
    password: str


class UserLoginDTO(BaseModel):
    account: str = Field(description='邮箱或手机号')
    password: str = Field(description='密码')
