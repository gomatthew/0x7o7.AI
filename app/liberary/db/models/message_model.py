import datetime

from sqlalchemy import Column, DateTime, String, Integer, func, Text
from sqlmodel import SQLModel, Field


class MessageModel(SQLModel, table=True):
    __tablename__ = 'message'
    message_id: str = Field(sa_type=String(32), primary_key=True, sa_column_kwargs={"comment": "主键id"})
    message_type: str = Field(sa_type=String(16), sa_column_kwargs={"comment": "消息类型"})
    conversation_id: str = Field(sa_type=String(32), sa_column_kwargs={"comment": "消息id"})
    user_id: str = Field(sa_type=String(32), sa_column_kwargs={"comment": "用户id"})
    user_query: str = Field(sa_type=Text, sa_column_kwargs={"comment": "用户输入"})
    ai_response: str = Field(sa_type=Text, nullable=True, sa_column_kwargs={"comment": "ai回复"})
    create_user: str = Field(sa_type=String(16), sa_column_kwargs={"comment": "创建人"})
    update_user: str = Field(sa_type=String(16), nullable=True, sa_column_kwargs={"comment": "更新人"})
    create_time: str = Field(sa_type=DateTime, sa_column_kwargs={"comment": "创建时间"},
                             default=func.now())
    update_time: str = Field(sa_type=DateTime, nullable=True, sa_column_kwargs={"comment": "更新时间"},
                             default=func.now())
    delete_tag: int = Field(default=0, sa_type=Integer, sa_column_kwargs={"comment": "删除标记 0-未删除 1-删除"})
