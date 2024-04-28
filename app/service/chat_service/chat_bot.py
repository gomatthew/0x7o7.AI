# -*- coding: utf-8 -*-
import asyncio
import json
from fastapi import Request, Body
from app import app
from app.utils import wrap_done
from app.dto.response_dto import BaseResponse
from sse_starlette.sse import EventSourceResponse
from app.service.model_service.model_service import get_hugging_face_llm
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.callbacks import AsyncIteratorCallbackHandler
from app.liberary.prompts.prompt_template import PROMPT_TEMPLATE


async def chat_bot(request: Request,
                   query: str = Body(..., description='user query'),
                   conversation_id: str = Body('', description='Conversation Id'),
                   prompt_template: str = Body('default', description='prompt_template'),
                   model_name: str = Body(app.config.get('LLM_MODELS')[0], description='LLM Model Name'),
                   # temperature: float = Body(app.config.get('TEMPERATURE'), description='Model Temperature'),
                   stream: bool = Body(True, description='Stream Output')):
    llm = get_hugging_face_llm(model_name)
    custom_prompt = PROMPT_TEMPLATE.get(prompt_template, 'default')
    prompt = PromptTemplate.from_template(custom_prompt)
    chain = LLMChain(llm=llm, promtp=prompt)
    callback = AsyncIteratorCallbackHandler()

    async def chat_iterator():
        task = asyncio.create_task((wrap_done(
            chain.acall({"input": query}),
            callback.done)))
        if stream:
            async for token in callback.aiter():
                yield json.dumps({'status': 200, 'message': 'success', 'data': {'token': token}})
        else:
            answer = ''
            async for token in callback.aiter():
                answer += token
            yield json.dumps({'status': 200, 'message': 'success', 'data': {'token': answer}})
        await task

    return EventSourceResponse(chat_iterator())
