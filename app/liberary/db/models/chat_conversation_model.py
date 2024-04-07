import datetime

from sqlalchemy import DateTime, String, Integer, func, Text
from sqlmodel import SQLModel, Field


class ConversationModel(SQLModel, table=True):
    conversation_id: str = Field(sa_type=String(32), primary_key=True, description="ID", alias='主键id',
                                 sa_column_kwargs={"comment": "id"})
    user_id: str = Field(sa_type=String(32), alias='用户id', sa_column_kwargs={"comment": "用户id"})
    user_query: str = Field(sa_type=Text, alias='用户输入', sa_column_kwargs={"comment": "用户输入"})
    ai_response: str = Field(sa_type=Text, alias='ai回复', sa_column_kwargs={"comment": "ai回复"})
    create_user: str = Field(sa_type=String(16), sa_column_kwargs={"comment": "创建人"})
    update_user: str = Field(sa_type=String(16), sa_column_kwargs={"comment": "更新人"})
    create_time: datetime.datetime = Field(sa_type=DateTime, sa_column_kwargs={"comment": "创建时间"},
                                           default=func.now())
    update_time: datetime.datetime = Field(sa_type=DateTime, sa_column_kwargs={"comment": "更新时间"},
                                           default=func.now())
    delete_tag: int = Field(sa_type=Integer, sa_column_kwargs={"comment": '删除标记 0-未删除 1-删除'})
