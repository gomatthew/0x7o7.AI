# -*- coding: utf-8 -*-
from pydantic import BaseModel


class TokenDTO(BaseModel):
    access_token: str
    token_type: str


class UserDTO(BaseModel):
    username: str
    email: str
    phone: str
    password: str
