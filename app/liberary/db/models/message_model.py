from sqlalchemy import Column, DateTime, String, Integer, func, Text
from sqlmodel import SQLModel


class MessageModel(SQLModel, table=True):
    message_id = Column(String(32), primary_key=True, comment='主键id')
    message_type = Column(String(8), comment='消息类型')
    conversation_id = Column(String(32), comment='主键id')
    user_id = Column(String(32), comment='主键id')
    user_query = Column(Text, comment='用户输入')
    ai_response = Column(Text, comment='ai回复')
    create_user = Column(String(16), comment='创建人')
    update_user = Column(String(16), comment='更新人')
    create_time = Column(DateTime, default=func.now(), comment='创建时间')
    update_time = Column(DateTime, default=func.now(), comment='更新时间')
    delete_tag = Column(Integer, comment='删除标记 0-未删除 1-删除')
