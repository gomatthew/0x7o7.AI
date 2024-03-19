from sqlalchemy import Column, DateTime, String, Integer, func
from app.liberary.db.base import Base


class User(Base):
    user_id = Column(String(32), primary_key=True, comment='用户id')
    user_name = Column(String(16), comment='用户名')
    user_phone = Column(String(16), comment='手机号')
    user_email = Column(String(32), comment='用户邮箱')
    user_type = Column(String(8), comment='用户类型 0-sup,1-normal,2-other')
    user_status = Column(Integer, comment='用户状态 1-正常，0-消极用户')
    create_user = Column(String(16), comment='创建人')
    update_user = Column(String(16), comment='更新人')
    create_time = Column(DateTime, default=func.now(), comment='创建时间')
    update_time = Column(DateTime, default=func.now(), comment='更新时间')
    delete_tag = Column(Integer, comment='删除标记 0-未删除 1-删除')
