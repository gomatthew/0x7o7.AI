# -*- coding: utf-8 -*-
import torch
from langchain.llms.base import LLM
from transformers import pipeline

class FlanLLM(LLM):
    llm_model_name: str = "google/flan-t5-xl"
    pipeline = pipeline("text2text-generation", model=llm_model_name, device="cuda:0", model_kwargs={"torch_dtype":torch.bfloat16})

    def _call(self, prompt, stop=None):
        return self.pipeline(prompt, max_length=9999)[0]["generated_text"]

    def _identifying_params(self):
        return {"name_of_model": self.llm_model_name}

    def _llm_type(self):
        return "custom"