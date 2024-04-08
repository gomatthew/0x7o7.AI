# -*- coding: utf-8 -*-
from langchain.memory import ChatMessageHistory
history = ChatMessageHistory()
history.add_user_message()
history.add_ai_message()
def make_chat_history():
    history.add