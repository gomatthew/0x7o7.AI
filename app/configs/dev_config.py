import os
import sys
from .base_config import Config


class DevConfig(Config):
    # MySQL
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:makemoney@127.0.0.1:3306/0x7o7_ai_dev"
    # SQLALCHEMY_BINDS = {
    #     'xxx': 'xxx',
    #     'xxxx': 'xxx'
    # }

    # CORS
    OPEN_CORS = True

    # Model Settings
    LLM_MODELS = ["Qwen-1_8B-Chat", ""]
    DEFAULT_DEVICE = "auto"
