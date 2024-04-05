# -*- coding: utf-8 -*-
import datetime
import uuid
from sqlmodel import Field, SQLModel
from sqlalchemy import DATETIME, String, func, Column


class UserModel(SQLModel, table=True):
    id: int = Field(primary_key=True, description="ID")
    username: str = Field(sa_type=String(32), description="用户名")
    password: str = Field(sa_type=String(64), description="hash_password")
    email: str = Field(sa_type=String(64), description='Email', unique=True)
    phone: str = Field(sa_type=String(16), description='手机号')
    status: int = Field(default=1, description='0-非活跃 1-活跃')
    token: int = Field(sa_type=String(64), description='token')
    salt: str = Field(sa_type=String(64), description='盐')
    create_time: datetime.datetime = Field(sa_type=DATETIME, default=func.now(), description="创建时间")
    update_time: datetime.datetime = Field(sa_type=DATETIME, default=func.now(), description="更新时间")
    version_id: str = Column(String(64))
    __mapper_args__ = {
        "version_id_col": version_id,
        "version_id_generator": lambda version: uuid.uuid4().hex
    }

    def __repr__(self):
        return self.id
