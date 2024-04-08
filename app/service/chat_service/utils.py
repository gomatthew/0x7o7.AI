# -*- coding: utf-8 -*-
from typing import List, Dict
from langchain.memory import ChatMessageHistory
from app.dto.chat_dto import ChatHistory
from app.liberary.enum.chat_enum import ChatRoleEnum



def make_chat_history(chat_history: List[ChatHistory], history_len: int = 3):
    __chat_history__ = ChatMessageHistory()
    history_len = history_len * 2
    chat_history = chat_history[-history_len:]
    for history in chat_history:
        match history.role:
            case ChatRoleEnum.AI.name:
                __chat_history__.add_ai_message(history.content)
            case ChatRoleEnum.USER.name:
                __chat_history__.add_user_message(history.content)
    return __chat_history__
