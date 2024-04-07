import os
import uvicorn
from multiprocessing import Process
from fastapi import FastAPI
from app import app
from app.routers import user_router

# 注册路由
app.include_router(user_router)


def start_models():
    # 起进程，记录进程id，将进程信息保存在redis。
    llm_model = app.config.get('LLM_MODELS')
    model_root_path = app.config.get('MODEL_ROOT_PATH')
    llm_model_dict = dict()
    if llm_model:
        for model_name in llm_model:
            llm_model_dict[model_name] = {'path': os.path.join(model_root_path, model_name)}


def main():
    if app.debug:
        uvicorn.run("main:app", host='127.0.0.1', port=8081, reload=True, workers=1)
    else:
        uvicorn.run("main:app", host='127.0.0.1', port=8081, reload=True, workers=1)


if __name__ == '__main__':
    main()
