from base_config import Config


class DevConfig(Config):


    # MySQL
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:makemoney@127.0.0.1:3306/aitest"

    MODEL_ROOT_PATH = ''

