import os
import uvicorn
from multiprocessing import Process
# from fastapi import FastAPI
from app import app
from app.routers import router_index
from app.service.model_service.model_service import start_model

# 注册路由
app.include_router(router_index)


# def make_llm_run():
#     llm_model = app.config.get('LLM_MODELS')
#     model_dict = dict()
#     for model_name in llm_model:
#         model_dict[model_name] = start_model(model_name)
#     app.llm_model = model_dict


def main():
    # make_llm_run()
    if app.debug:
        uvicorn.run("main:app", host='127.0.0.1', port=8081, reload=True, workers=1)
    else:
        uvicorn.run("main:app", host='127.0.0.1', port=8081, reload=True, workers=1)


if __name__ == '__main__':
    main()
