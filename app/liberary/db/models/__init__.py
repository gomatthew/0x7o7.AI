# -*- coding: utf-8 -*-
from app.liberary.db.base import engine

if __name__ == '__main__':
    from chat_conversation_model import *
    from user_model import *
    from file_model import *
    from message_model import *

    SQLModel.metadata.create_all(engine)
