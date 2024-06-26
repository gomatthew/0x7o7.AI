# -*- coding: utf-8 -*-
import asyncio
import json
from fastapi import Request, Body
from sse_starlette.sse import EventSourceResponse
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.callbacks import AsyncIteratorCallbackHandler
from app import app
from app.dto.response_dto import BaseResponse
# from app.routers.router import chat_router as router
from app.router import chat_router as router
from app.utils import wrap_done
# from app.service.model_service.model_service import get_hugging_face_llm
from app.liberary.prompts.prompt_template import PROMPT_TEMPLATE
from app.service.chat_service.utils import make_chat_history_by_user_id
from app.liberary.enum.chat_type_enum import ChatTypeEnum
from app.liberary.db.repository.message_repository import add_message_to_db
from app.liberary.db.repository.conversation_repository import add_conversation_to_db
from app.liberary.callback_handler.conversation_callback_handler import ConversationCallbackHandler
from llm_model_worker import LLM_MODELS


# 将hugging face model 集成到 langchain里
# https://python.langchain.com/docs/integrations/llms/huggingface_pipelines/


@router.post('/llm/chat')
async def chat_bot(request: Request,
                   query: str = Body(..., description='user query'),
                   conversation_id: str = Body('', description='Conversation Id'),
                   prompt_template: str = Body('default', description='prompt_template'),
                   llm_model_name: str = Body(LLM_MODELS[0], description='LLM Model Name'),
                   memory: bool = Body(False, description='need memory'),
                   # temperature: float = Body(app.config.get('TEMPERATURE'), description='Model Temperature'),
                   stream: bool = Body(True, description='Stream Output')):
    # if not llm:
    #     return BaseResponse(status=200,
    #                         message=f'{llm_model_name} is not available, available model:{list(app.model.keys())}')
    chat_history = None
    if not conversation_id:
        conversation_id = add_conversation_to_db(user_id='user_id', user_query=query, create_user='0x7o7')
    message_id = add_message_to_db(message_type=ChatTypeEnum.TEXT_CHAT.name, conversation_id=conversation_id,
                                   user_id='user_id', user_query=query, create_user='0x7o7')
    llm = app.llm.get(llm_model_name)
    custom_prompt = PROMPT_TEMPLATE.get('chat_bot', 'default')
    prompt = PromptTemplate.from_template('{input}')
    if memory:
        chat_history = make_chat_history_by_user_id(user_id='user_id', message_type=ChatTypeEnum.TEXT_CHAT.name,
                                                    history_len=3)
    chain = LLMChain(llm=llm.get_llm(), prompt=prompt, memory=chat_history)
    async_callback = AsyncIteratorCallbackHandler()
    custom_callback = ConversationCallbackHandler(conversation_id=conversation_id, message_id=message_id,
                                                  chat_type=ChatTypeEnum.TEXT_CHAT.name, query=query)
    callbacks = [async_callback, custom_callback]

    async def chat_iterator():
        task = asyncio.create_task((wrap_done(
            chain.ainvoke({"input": query}, config=callbacks),
            async_callback.done)))
        if stream:
            async for token in async_callback.aiter():
                print(123)
                yield json.dumps({'status': 200, 'message': 'success', 'data': {'token': token}})

        else:
            answer = ''
            async for token in async_callback.aiter():
                answer += token
            yield json.dumps({'status': 200, 'message': 'success', 'data': {'token': answer}})
        await task

    return EventSourceResponse(chat_iterator())
