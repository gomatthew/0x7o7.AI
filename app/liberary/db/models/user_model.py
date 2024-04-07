# -*- coding: utf-8 -*-
import datetime
import uuid
from sqlmodel import Field, SQLModel
from sqlalchemy import DateTime, String, func, Column


class UserModel(SQLModel, table=True):
    id: int = Field(primary_key=True, description="ID")
    username: str = Field(sa_type=String(32), description="用户名", sa_column_kwargs={"comment": "用户名"})
    password: str = Field(sa_type=String(64), description="hash_password",
                          sa_column_kwargs={"comment": "hash_password"})
    email: str = Field(sa_type=String(64), description='Email', unique=True, sa_column_kwargs={"comment": "Email"})
    phone: str = Field(sa_type=String(16), description='手机号', sa_column_kwargs={"comment": "手机号"})
    status: int = Field(default=1, description='0-非活跃 1-活跃', sa_column_kwargs={"comment": "0-非活跃 1-活跃"})
    token: int = Field(sa_type=String(256), description='token', default=None, nullable=True,
                       sa_column_kwargs={"comment": "token"})
    salt: str = Field(sa_type=String(64), description='盐', sa_column_kwargs={"comment": "盐"})
    create_time: datetime.datetime = Field(sa_type=DateTime, default=func.now(), description="创建时间",
                                           sa_column_kwargs={"comment": "创建时间"})
    update_time: datetime.datetime = Field(sa_type=DateTime, default=func.now(), description="更新时间",
                                           sa_column_kwargs={"comment": "更新时间"})
    create_user: str = Field(sa_type=String(16), sa_column_kwargs={"comment": "创建人"})
    update_user: str = Field(sa_type=String(16), nullable=True, default=None, sa_column_kwargs={"comment": "更新人"})
    # version_id: str = Column(String(64))

    # __mapper_args__ = {
    #     "version_id_col": version_id,
    #     "version_id_generator": lambda version: uuid.uuid4().hex
    # }

    def __repr__(self):
        return self.id
