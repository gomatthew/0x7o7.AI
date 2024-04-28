import datetime

from sqlalchemy import Column, DateTime, String, Integer, func
from sqlmodel import SQLModel, Field


class FileModel(SQLModel, table=True):
    __tablename__ = 'file'
    file_id: str = Field(sa_type=String(32), primary_key=True, sa_column_kwargs={"comment": "主键id"})
    message_id: str = Field(sa_type=String(32), sa_column_kwargs={"comment": "消息id"})
    user_id: str = Field(sa_type=String(32), sa_column_kwargs={"comment": "用户id"})
    file_type: str = Field(sa_type=String(32), sa_column_kwargs={"comment": "文件类型"})
    file_path: str = Field(sa_type=String(512), sa_column_kwargs={"comment": "文件保存路径"})
    create_user: str = Field(sa_type=String(16), sa_column_kwargs={"comment": "创建人"})
    update_user: str = Field(sa_type=String(16), sa_column_kwargs={"comment": "更新人"})
    create_time: datetime.datetime = Field(sa_type=DateTime, sa_column_kwargs={"comment": "创建时间"},default=func.now())
    update_time: datetime.datetime = Field(sa_type=DateTime, sa_column_kwargs={"comment": "更新时间"},default=func.now())
    delete_tag: int = Field(sa_type=Integer, sa_column_kwargs={"comment": "删除标记 0-未删除 1-删除"})
