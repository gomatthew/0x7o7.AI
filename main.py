import uvicorn
import os
from app import app

from app.routers import user_router
# app = create_app(os.getenv('RUNTIME_ENV'))
# # 注册路由
app.include_router(user_router)


# app.include_router(chat_router)
# app.include_router(llm_model_router)
# app.include_router(doc_router)


def main():
    if app.debug:
        uvicorn.run("main:app", host='127.0.0.1', port=8081, reload=True, workers=1)
    else:
        uvicorn.run("main:app", host='127.0.0.1', port=8081, reload=True, workers=1)


if __name__ == '__main__':
    main()
