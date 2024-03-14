from fastapi import FastAPI
from app.controller import test_router
from app.configs import get_config_by_env


def create_app(env):
    config = get_config_by_env(env)
    _app = FastAPI()
    _app.include_router(test_router)
    _app.__setattr__("config", config)
    return _app


