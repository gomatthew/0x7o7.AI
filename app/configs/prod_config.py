from app.configs.base_config import Config


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI: str = 'mysql+pymysql://root:makemoney@127.0.0.1:3306/0x7o7_ai'
    OPEN_CORS: bool = True
