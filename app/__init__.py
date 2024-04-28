# -*- coding: utf-8 -*-
import os
import logging
import uuid
import traceback
import redis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.configs import get_config_by_env
from app.liberary.logger import get_logger
# from app.service.model_service.model_service import start_model
__version__ = '0.0.1'


# 🟢
# 🔴
# def get_logger(logger_level):
#     logger = logging.getLogger()
#     handler = logging.StreamHandler()
#     formatter = logging.Formatter('%(asctime)s - %(module)s - [%(levelname)s] : %(message)s',
#                                   datefmt='%Y-%m-%d %H:%M:%S %p', )
#     handler.setFormatter(formatter)
#     logger.addHandler(handler)
#     logger.setLevel(logger_level)
#     return logger


def create_app(env='dev'):
    app = FastAPI(
        title='AI 0x7o7',
        summary='LLM Model Service',
        version=__version__
    )
    config = get_config_by_env(env)

    if config.OPEN_CORS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    app.seed = uuid.uuid4().hex
    app.config = config.dict()
    app.logger = get_logger(app.config.get('LOG_LEVEL'))
    app.redis = redis.from_url(app.config.get('REDIS_URL'))
    # llm_model = app.config.get('LLM_MODELS')
    # model_dict = dict()
    # for model_name in llm_model:
    #     model_dict[model_name] = start_model(model_name)
    # app.llm_model = model_dict
    # app.__setattr__("config", config.dict())
    # _logger = get_logger(app.config.get('LOG_LEVEL'))
    # app.__setattr__('logger', _logger)
    return app


app = create_app(os.getenv('RUNTIME_ENV'))
# from app.service.router import user_router
