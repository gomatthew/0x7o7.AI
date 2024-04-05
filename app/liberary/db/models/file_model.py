from sqlalchemy import Column, DateTime, String, Integer, func
from sqlmodel import SQLModel

class FileModel(SQLModel,table=True):
    file_id = Column(String(32), primary_key=True, comment='主键id')
    message_id = Column(String(32), comment='消息id')
    user_id = Column(String(32), comment='用户id')
    file_type = Column(String(8), comment='文件类型')
    file_path = Column(String(256), comment='文件保存路径')
    create_user = Column(String(16), comment='创建人')
    update_user = Column(String(16), comment='更新人')
    create_time = Column(DateTime, default=func.now(), comment='创建时间')
    update_time = Column(DateTime, default=func.now(), comment='更新时间')
    delete_tag = Column(Integer, comment='删除标记 0-未删除 1-删除')
