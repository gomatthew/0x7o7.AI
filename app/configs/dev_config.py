import os
import sys
from .base_config import Config


class DevConfig(Config):
    # MySQL
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:makemoney@127.0.0.1:3306/aitest"

    MODEL_ROOT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'models')

    # Model Settings
    LLM_MODELS = ["Qwen-1_8B-Chat"]
    DEFAULT_DEVICE = "auto"
    # 各服务器默认绑定host。如改为"0.0.0.0"需要修改下方所有XX_SERVER的host
    DEFAULT_BIND_HOST = "0.0.0.0" if sys.platform != "win32" else "127.0.0.1"
    MODEL_WORKER = {
        "default": {
            "host": DEFAULT_BIND_HOST,
            "port": 17777,
            "DEVICE": DEFAULT_DEVICE,
            "infer_turbo": False,
            "gpus": None,  # "0,1"
            "nums_gpus": 1,
            # "max_gpu_memory": "20GiB", # 每个GPU占用的最大显存
            # 以下为model_worker非常用参数，可根据需要配置
            # "load_8bit": False, # 开启8bit量化
            # "cpu_offloading": None,
            # "gptq_ckpt": None,
            "gptq_wbits": 16,
            # "gptq_groupsize": -1,
            # "gptq_act_order": False,
            # "awq_ckpt": None,
            "awq_wbits": 16,
            # "awq_groupsize": -1,
            # "model_names": LLM_MODELS,
            # "conv_template": None,
            # "limit_worker_concurrency": 5,
            # "stream_interval": 2,
            # "no_register": False,
            # "embed_in_truncate": False,

        },

    }

# if __name__ == '__main__':
