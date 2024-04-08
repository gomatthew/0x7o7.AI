# -*- coding: utf-8 -*-
import os
import traceback

from app import app
from typing import Union
from langchain import HuggingFacePipeline



def model_factory(model_name) -> Union[callable, str]:
    # 起进程，记录进程id，将进程信息保存在redis。
    model_key: str = ''
    llm_model = app.config.get('LLM_MODELS')
    if model_name not in llm_model:
        return f'{model_name} is not '
    llm_model_factory = app.config.get('LLM_MODEL_FACTORY')
    for k, v in llm_model_factory.values():
        if model_name in v:
            model_key = k
    match model_key:
        case 'Qwen':
            from app.liberary.model_worker.qwen import QwenModelWorker
            return QwenModelWorker(model_name)  # 有1.8B-7B 所以需要传入不同的model_name
        case _:
            return f'{model_name} is not available'


def start_model(model_name):
    app.logger.info(f'🟢 Start model :{model_name}')
    try:
        model_instance = model_factory(model_name)
        if isinstance(model_instance, str):
            return f'{model_name} is not available'
        model = model_instance.lunch_model()
        # process = Process(
        #     target=model_instance.lunch_model(),
        #     name=f'model_worker_{model_name}',
        #     # kwargs=,
        #     daemon=True,
        # )
        # process.start()
        # app.redis.hset(app.seed, f'{model_name}_worker_process', process)
        app.redis.hset('AI Service', f'{model_name}_worker_instance_{app.seed}', model)
        app.logger.info(f'🟢 Start model :{model_name} success.')
    except BaseException as e:
        app.logger.error(f'🔴 Start model :{model_name} failed.')
        app.logger.error(traceback.format_exc())
        app.logger.error(e)


def get_model_by_name(model_name):
    model = app.redis.hget('AI Service', f'{model_name}_worker_instance_{app.seed}')
    return model


def get_langchain_llm(model_name):


    llm = HuggingFacePipeline.from_model_id(model_id="bigscience/bloom-1b7", task="audio-classification",
                                            model_kwargs={"temperature": 0, "max_length": 64})

    # # https://huggingface.co/docs/transformers/main_classes/pipelines
    # model_id = "gpt2"
    # tokenizer = AutoTokenizer.from_pretrained(model_id)
    # model = AutoModelForCausalLM.from_pretrained(model_id)
    # pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=10)
    # hf = HuggingFacePipeline(pipeline=pipe)
    #
    # from langchain_core.prompts import PromptTemplate
    #
    # template = """Question: {question}
    #
    # Answer: Let's think step by step."""
    # prompt = PromptTemplate.from_template(template)
    #
    # chain = prompt | hf
    #
    # question = "What is electroencephalography?"
    #
    # print(chain.invoke({"question": question}))
    # pass
    #
    # # https://github.com/langchain-ai/langchain/discussions/17637
    # from transformers import AutoModelForCausalLM, AutoTokenizer
    #
    # model_id = "<your_local_model_directory>"
    # tokenizer = AutoTokenizer.from_pretrained(model_id)
    # model = AutoModelForCausalLM.from_pretrained(model_id)
    # from transformers import pipeline
    #
    # pipe = pipeline(
    #     "text-generation", model=model, tokenizer=tokenizer, max_new_tokens=10
    # )
    # from langchain_community.llms.self_hosted import SelfHostedPipeline
    # from langchain_community.hardware import get_remote_instance
    #
    # gpu = get_remote_instance()
    # llm = SelfHostedPipeline.from_pipeline(
    #     pipeline=pipe,
    #     hardware=gpu,
    # )
    #
    # from langchain_community.llms import CTransformers