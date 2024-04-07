# -*- coding: utf-8 -*-

from app import app
from abc import abstractmethod, ABCMeta


class ModelWorkerBase(object, metaclass=ABCMeta):
    def __init__(self):
        self.model_name = ''
        self.device = app.config.get('LLM_DEVICE')
        self.model_root_path = app.config.get('MODEL_ROOT_PATH')
        # self.model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen1.5-7B-Chat", device_map="auto")
        # self.tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen1.5-7B-Chat")

    @abstractmethod
    def lunch_model(self):
        pass
