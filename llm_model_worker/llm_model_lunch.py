# -*- coding: utf-8 -*-
from llm_model_worker import LLM_MODELS
from llm_model_worker.llm_model_factory import model_factory


def init_llm_lunch():
    model_instance = dict()
    for llm in LLM_MODELS:
        model_worker = model_factory(llm)
        model_instance[llm] = model_worker
        return model_instance
