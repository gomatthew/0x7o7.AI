"""
Base Config
"""
import os


class Config(object):
    """
    Configs that include all the configurable settings
    """

    def __init__(self, environment=None):
        self.environment = environment

    SECRET_KEY = "9&l@xuFGa7ND^fq&YZ*LYUXE5a^n__MATTHEW_ALLWAYS_WIN__EVFKdT@nMrbEA!#r!2Y0EwPnRu1^dhCDk!4L"
    # Model Settings
    TEMPERATURE = 0.17
    MODEL_ROOT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'llm_models')

    # DB Settings
    SQLALCHEMY_DATABASE_URI = 'mysql://root:xxxx@127.0.0.1:3306/xxxx'
    SQLALCHEMY_BINDS = {
        'xxx': 'xxx',
        'xxxx': 'xxx'
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 200,
        'pool_recycle': 120,
        'pool_pre_ping': True
    }
    SQLALCHEMY_ECHO = False  # echo SQL info

    # Redis Settings
    REDIS_URL = "redis://xx:xx/xx"
    RQ_REDIS_URL = REDIS_URL
    REDIS_DEFAULT_TTL = 86400

    # Logging
    DEBUG = True
    LOG_LEVEL = 'INFO'

    # RQ Settings, must start from 0
    QUEUES = [f'ai_queue_{i}' for i in range(10)]
    RQ_MAX_RETRIES = 5
    RQ_QUEUE_PREFIX = "es_queue_"

    # ElasticSearch
    ELASTICSEARCH_HOST = "xx.xx.xx.xxx:xx"
    ELASTICSEARCH_HTTP_AUTH = None
    ES_INDEX_PREFIX = 'xxx_'
    ES_DEFAULT_SHARDS = 3
    ES_DEFAULT_REPLICAS = 1
    ES_INDEX = ['']


if __name__ == '__main__':
    print(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'llm_models'))
