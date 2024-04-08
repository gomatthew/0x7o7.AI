# -*- coding: utf-8 -*-
from fastapi import Request, Body
from app import app
from app.liberary.model_worker import get_model_by_name

async def chat_bot(request: Request,
                   conversation_id: str = Body('', description='Conversation Id'),
                   model_name: str = Body(app.config.get('LLM_MODELS')[0], description='LLM Model Name'),
                   temperature: float = Body(app.config.get('TEMPERATURE'), description='Model Temperature'),
                   stream: bool = Body(True, description='Stream Output')):
    model = get_model_by_name(model_name)
    return
