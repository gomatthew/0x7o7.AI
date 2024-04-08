# -*- coding: utf-8 -*-
import os
import traceback

from app import app
from multiprocessing import Process
from typing import Union


def model_factory(model_name) -> Union[callable, str]:
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
            return QwenModelWorker(model_name)  # 有1.8B-7B 所以需要传入不同的model_name
        case _:
            return f'{model_name} is not available'


def start_model(model_name):
    app.logger.info(f'🟢 Start model :{model_name}')
    try:
        model_instance = model_factory(model_name)
        if isinstance(model_instance, str):
            return f'{model_name} is not available'
        model = model_instance.lunch_model()
        # process = Process(
        #     target=model_instance.lunch_model(),
        #     name=f'model_worker_{model_name}',
        #     # kwargs=,
        #     daemon=True,
        # )
        # process.start()
        # app.redis.hset(app.seed, f'{model_name}_worker_process', process)
        app.redis.hset('AI Service', f'{model_name}_worker_instance_{app.seed}', model)
        app.logger.info(f'🟢 Start model :{model_name} success.')
    except BaseException as e:
        app.logger.error(f'🔴 Start model :{model_name} failed.')
        app.logger.error(traceback.format_exc())
        app.logger.error(e)


def get_model_by_name(model_name):
    model = app.redis.hget('AI Service', f'{model_name}_worker_instance_{app.seed}')
    return model
