"""
Base Config
"""
import os
from pydantic_settings import BaseSettings
from typing import Dict, List, Union


class Config(BaseSettings):
    """
    Configs that include all the configurable settings
    """

    SECRET_KEY: str = "9&l@xuFGa7ND^fq&YZ*LYUXE5a^n__MATTHEW_ALLWAYS_WIN__EVFKdT@nMrbEA!#r!2Y0EwPnRu1^dhCDk!4L"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = 'HS256'

    # DB Settings
    SQLALCHEMY_DATABASE_URI: str = 'mysql://root:xxxx@127.0.0.1:3306/xxxx'
    SQLALCHEMY_BINDS: Dict = {
        'xxx': 'xxx',
        'xxxx': 'xxx'
    }
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SQLALCHEMY_ENGINE_OPTIONS: Dict = {
        'pool_size': 200,
        'pool_recycle': 120,
        'pool_pre_ping': True
    }
    SQLALCHEMY_ECHO: bool = False  # echo SQL info

    # Redis Settings
    REDIS_URL: str = "redis://xx:xx/xx"
    REDIS_DEFAULT_TTL: int = 86400

    # Logging
    DEBUG: bool = True
    LOG_LEVEL: str = 'INFO'

    # RQ Settings, must start from 0
    QUEUES: List[str] = [f'ai_queue_{i}' for i in range(10)]
    RQ_MAX_RETRIES: int = 5
    RQ_QUEUE_PREFIX: str = "ai_queue_"

    # ElasticSearch
    ELASTICSEARCH_HOST: str = "xx.xx.xx.xxx:xx"
    ELASTICSEARCH_HTTP_AUTH: Union[str, None] = None
    ES_INDEX_PREFIX: str = 'xxx_'
    ES_DEFAULT_SHARDS: int = 3
    ES_DEFAULT_REPLICAS: int = 1
    ES_INDEX: List[str] = ['']


if __name__ == '__main__':
    print(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'llm_models'))
