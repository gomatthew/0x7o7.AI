import os
import uvicorn
from multiprocessing import Process
from app import app
from app.service import router

# 注册路由
app.include_router(router)

# def make_llm_run():
#     llm_model = app.config.get('LLM_MODELS')
#     model_dict = dict()
#     for model_name in llm_model:
#         model_dict[model_name] = start_model(model_name)
#     app.llm_model = model_dict


def main():
    if app.debug:
        uvicorn.run(app, host='127.0.0.1', port=8081,
                    # reload=True,
                    workers=1
                    )
    else:
        uvicorn.run(app, host='127.0.0.1', port=8081,
                    # reload=True,
                    workers=1
                    )


if __name__ == '__main__':
    # init_llm_lunch()
    # uvicorn.run("main:app", host='127.0.0.1', port=8081, reload=True, workers=1)
    main()