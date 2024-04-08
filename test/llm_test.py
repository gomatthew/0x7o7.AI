# -*- coding: utf-8 -*-
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline

# from transformers import
llm = HuggingFacePipeline.from_model_id(model_id=r'D:\deep_learning_model\Qwen\Qwen-1_8B-Chat', task='text-generation',
                                        model_kwargs={"temperature": 0,
                                                      "max_length": 64, 'trust_remote_code': True, 'do_sample': True})

print(llm)
