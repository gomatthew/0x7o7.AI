# -*- coding: utf-8 -*-
# from fastapi import APIRouter
from .chat_service.chat_bot import chat_bot
from .user_service.user_handle import add_user
from .user_service.auth_handle import user_login
# user_router = APIRouter(
#     prefix='/user',
#     tags=['User']
# )


# chat_router = APIRouter(
#     prefix='/chat',
#     tags=['LLM Chat'],
# )
#
# llm_model_router = APIRouter(
#     prefix='/llm/model',
#     tags=['LLM Models']
# )
