# -*- coding: utf-8 -*-
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

llm = HuggingFacePipeline.from_model_id(model_id='/data/ai/llm/models/Qwen1.5-7B-Chat', task='text-generation',
                                        device_map='auto',
                                        model_kwargs={"temperature": 0.1,
                                                      "max_length": 64, 'trust_remote_code': True},
                                        pipeline_kwargs={"max_new_tokens": 10})
prompt_template = "Tell me a {adjective} joke"

prompt = PromptTemplate.from_template(prompt_template)

chain = prompt | llm
chain.invoke({'adjective': 'socks'})
