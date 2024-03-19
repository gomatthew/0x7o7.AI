import uuid
from app.liberary.db.session import with_session
from app.liberary.db.models.chat_conversation_model import ConversationModel
from sqlalchemy import and_


@with_session
def add_conversation_to_db(session, user_id, user_query="", conversation_id=None) -> str:
    """
    新增聊天对话
    """

    # 非首次对话
    query = session.query(ConversationModel).filter(
        and_(ConversationModel.conversation_id == conversation_id, ConversationModel.delete_tag == 0)).first()
    # 如果传入的conversation id 是已经删除的 conversation，那么和传空值效果相同，同样创建新对话，返回新id
    if query:
        return query.conversation_id

    if not conversation_id:
        conversation_id = uuid.uuid4().hex
    conversation_obj = ConversationModel(conversation_id=conversation_id, user_query=user_query, user_id=user_id, delete_tag=0)

    session.add(conversation_obj)
    session.commit()
    return conversation_id.conversation_id
