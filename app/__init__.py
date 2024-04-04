from fastapi import FastAPI
from app.controller import test_router
from app.configs import get_config_by_env
from fastapi.middleware.cors import CORSMiddleware

__version__ = '0.0.1'


def create_app(env='dev'):
    config = get_config_by_env(env)
    _app = FastAPI(
        title='AI 0x7o7',
        version='0.010'
    )
    if config.OPEN_CORS:
        _app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    _app.include_router(test_router)
    _app.__setattr__("config", config)
    return _app


app = create_app()
