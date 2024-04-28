# -*- coding: utf-8 -*-
from fastapi import APIRouter

user_router = APIRouter(
    prefix='/user',
    tags=['User']
)

chat_router = APIRouter(
    prefix='/chat',
    tags=['LLM Chat'],
)

llm_model_router = APIRouter(
    prefix='/llm/model',
    tags=['LLM Models']
)
