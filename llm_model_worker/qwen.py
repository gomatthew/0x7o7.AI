# -*- coding: utf-8 -*-
import os
from llm_model_worker.base import ModelWorkerBase
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from llm_model_worker import MODEL_CONFIG
from transformers import AutoTokenizer, AutoModelForCausalLM,pipeline


class QwenModelWorker(ModelWorkerBase):
    def __init__(self, llm_model_name):
        super().__init__()
        self.model_name = llm_model_name
        self.model_config = MODEL_CONFIG.get(llm_model_name)
        self.model_path = os.path.join(self.model_root_path, self.model_config.get('path'))
        self.model = AutoModelForCausalLM.from_pretrained(self.model_path, trust_remote_code=True,
                                                          device_map=self.model_config.get('device'))
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, trust_remote_code=True)
        self.worker = self.lunch_model()
    def lunch_model(self):

        pipe = pipeline('text-generation', model=self.model, tokenizer=self.tokenizer, max_new_tokens=100,
                        trust_remote_code=True)
        llm = HuggingFacePipeline(pipeline=pipe)

        # llm = HuggingFacePipeline.from_model_id(model_id=self.model_path, task=self.model_task, device_map='auto',
        #                                         model_kwargs={"temperature": self.temperature, 'do_sample': True,
        #                                                       "max_length": self.max_length,
        #                                                       'trust_remote_code': True},
        #                                         pipeline_kwargs={"max_new_tokens": 10})
        return llm

    def get_llm(self):
        return self.worker
# prompt = "Give me a short introduction to large language model."
#
# messages = [{"role": "user", "content": prompt}]
#
# text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
#
# model_inputs = tokenizer([text], return_tensors="pt").to(device)
#
# generated_ids = model.generate(model_inputs.input_ids, max_new_tokens=512, do_sample=True)
#
# generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)]
#
# response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
