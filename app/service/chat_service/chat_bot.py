# -*- coding: utf-8 -*-
from fastapi import Request, Body
from app import app
from app.dto.response_dto import BaseResponse


async def chat_bot(request: Request,
                   conversation_id: str = Body('', description='Conversation Id'),
                   model_name: str = Body(app.config.get('LLM_MODELS')[0], description='LLM Model Name'),
                   temperature: float = Body(app.config.get('TEMPERATURE'), description='Model Temperature'),
                   stream: bool = Body(True, description='Stream Output')):
    llm = app.model.get(model_name)
    if not llm:
        return BaseResponse(status=200,
                            message=f'{model_name} is not available, available model:{list(app.model.keys())}')

    return
