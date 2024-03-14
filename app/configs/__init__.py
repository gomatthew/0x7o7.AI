from .dev_config import DevConfig
from .prod_config import ProdConfig


def get_config_by_env(run_time_env):
    match run_time_env:
        case 'dev':
            return DevConfig()
        case 'prod':
            return ProdConfig()
        case _:
            raise Exception('wrong run time env')
