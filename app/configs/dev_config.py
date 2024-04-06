from .base_config import Config
from typing import List


class DevConfig(Config):
    # MySQL
    SQLALCHEMY_DATABASE_URI: str = "mysql+pymysql://root:makemoney@127.0.0.1:3306/0x7o7_ai_dev"
    # SQLALCHEMY_BINDS = {
    #     'xxx': 'xxx',
    #     'xxxx': 'xxx'
    # }

    # CORS
    OPEN_CORS: bool = True

    # Model Settings
    LLM_MODELS: List[str] = ["Qwen-1_8B-Chat"]
    DEFAULT_DEVICE: str = "auto"
