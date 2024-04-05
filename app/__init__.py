import logging
from fastapi import FastAPI
from app.controller import user_router, chat_router, llm_model_router
from app.configs import get_config_by_env
from fastapi.middleware.cors import CORSMiddleware

__version__ = '0.0.1'


# 🟢
# 🔴
def get_logger(logger_level):
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(module)s - [%(levelname)s] : %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S %p', )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logger_level)
    return logger


def create_app(env='dev'):
    config = get_config_by_env(env)
    _app = FastAPI(
        title='AI 0x7o7',
        version=__version__
    )
    if config.OPEN_CORS:
        _app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    _logger = get_logger(config.get('LOG_LEVEL'))
    _app.__setattr__('logger', _logger)
    _app.__setattr__("config", config)
    return _app


app = create_app()

# 注册路由
app.include_router(user_router)
app.include_router(chat_router)
app.include_router(llm_model_router)
