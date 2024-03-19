import uuid
from app.liberary.db.session import with_session
from app.liberary.db.models.message_model import MessageModel


@with_session
def add_message_to_db(session,message_type, conversation_id, user_id, user_query, create_user) -> str:
    """
    新增聊天详情
    """
    message_id = uuid.uuid4().hex
    __message = MessageModel(message_id=message_id, message_type=message_type, conversation_id=conversation_id,
                             user_id=user_id, user_query=user_query, create_user=create_user)
    session.add(__message)
    session.commit()
    return message_id
