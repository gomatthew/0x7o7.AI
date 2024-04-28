import uuid
from typing import Dict
from sqlalchemy import desc, and_
from app.liberary.db.session import with_session
from app.liberary.db.models.message_model import MessageModel


@with_session
def add_message_to_db(session, message_type, conversation_id, user_id, user_query, create_user) -> str:
    """
    新增聊天详情
    """
    message_id = uuid.uuid4().hex
    __message = MessageModel(message_id=message_id, message_type=message_type, conversation_id=conversation_id,
                             user_id=user_id, user_query=user_query, create_user=create_user)
    session.add(__message)
    session.commit()
    return message_id


@with_session
def get_chat_history_by_user_id(session, user_id, message_type, history_len):
    """
    根据用户id查询聊天历史记录
    """

    query = session.query(MessageModel).filter(
        and_(MessageModel.user_id == user_id, MessageModel.message_type == message_type)).order_by(
        desc(MessageModel.create_time)).limit(history_len).all()

    if query:
        return [(q.user_query, q.ai_response) for q in query]
    else:
        return None


@with_session
def get_message_by_id(session, message_id) -> MessageModel:
    """
    查询聊天记录
    """
    m = session.query(MessageModel).filter_by(id=message_id).first()
    return m


@with_session
def update_message(session, message_id, response: str = None, metadata: Dict = None, response_extension=None):
    """
    更新已有的聊天记录
    """
    m = get_message_by_id(message_id)
    if m is not None:
        if response is not None:
            m.response = response
        if isinstance(metadata, dict):
            m.meta_data = metadata
        if response_extension is not None:
            m.response_extension = response_extension
        session.add(m)
        session.commit()
        return m.id
