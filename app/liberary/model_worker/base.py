# -*- coding: utf-8 -*-

from app import app
from abc import abstractmethod, ABCMeta
from app.liberary.enum.pipeline_task_enum import PipeLineTaskEnum

'''
device (int or str or torch.device) — Defines the device (e.g., "cpu", "cuda:1", "mps", or a GPU ordinal rank like 1) on which this pipeline will be allocated.
device_map (str or Dict[str, Union[int, str, torch.device], optional) — Sent directly as model_kwargs (just a simpler shortcut). When accelerate library is present, set device_map="auto" to compute the most optimized device_map automatically (see here for more information).
Do not use device_map AND device at the same time as they will conflict
'''
# -*- coding: utf-8 -*-
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline


# from transformers import
# llm = HuggingFacePipeline.from_model_id(model_id=r'D:\deep_learning_model\Qwen\Qwen-1_8B-Chat', task='text-generation',
#                                         model_kwargs={"temperature": 0,
#                                                       "max_length": 64, 'trust_remote_code': True, 'do_sample': True})
#
# print(llm)


class ModelWorkerBase(object, metaclass=ABCMeta):
    def __init__(self):
        self.model_name = ''
        self.model_task = PipeLineTaskEnum.TEXT_GENERATION.value
        self.device = app.config.get('LLM_DEVICE')
        self.model_root_path = app.config.get('MODEL_ROOT_PATH')
        self.temperature = app.config.get('TEMPERATURE')
        self.max_length = app.config.get('MAX_LENGTH')
        # self.model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen1.5-7B-Chat", device_map="auto")
        # self.tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen1.5-7B-Chat")

    @abstractmethod
    def lunch_model(self):
        pass
