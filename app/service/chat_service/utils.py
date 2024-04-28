# -*- coding: utf-8 -*-
from typing import List
from langchain.memory import ChatMessageHistory
from app.dto.chat_dto import ChatHistory
from app.liberary.enum.chat_enum import ChatRoleEnum
from app.liberary.db.repository.message_repository import get_chat_history_by_user_id


def make_chat_history_by_user_id(user_id: str, message_type, history_len):
    db_query = get_chat_history_by_user_id(user_id=user_id, message_type=message_type, history_len=history_len)
    chat_history_list = list()
    for chat in db_query:
        chat_history_list.append(ChatHistory(role="USER", content=chat[0]))
        chat_history_list.append(ChatHistory(role="AI", content=chat[1]))
    return make_chat_history(chat_history_list)


def make_chat_history(chat_history: List[ChatHistory]):
    __chat_history__ = ChatMessageHistory()
    # history_len = history_len * 2
    # chat_history = chat_history[-history_len:]
    for history in chat_history:
        match history.role:
            case ChatRoleEnum.AI.name:
                __chat_history__.add_ai_message(history.content)
            case ChatRoleEnum.USER.name:
                __chat_history__.add_user_message(history.content)
    return __chat_history__
