# -*- coding: utf-8 -*-
import os
from app import app


def start_models(model_name):
    # 起进程，记录进程id，将进程信息保存在redis。
    model_key: str = ''
    llm_model = app.config.get('LLM_MODELS')
    if model_name not in llm_model:
        return f'{model_name} is not '
    llm_model_factory = app.config.get('LLM_MODEL_FACTORY')
    for k, v in llm_model_factory.values():
        if model_name in v:
            model_key = k
    match model_key:
        case 'Qwen':
            from app.liberary.model_worker.qwen import QwenModelWorker
        case _:
            return f'{model_name} is not available'
