import os
import uvicorn
from multiprocessing import Process
# from fastapi import FastAPI
from app import app
from app.routers import user_router

# 注册路由
app.include_router(user_router)


def main():
    if app.debug:
        uvicorn.run("main:app", host='127.0.0.1', port=8081, reload=True, workers=1)
    else:
        uvicorn.run("main:app", host='127.0.0.1', port=8081, reload=True, workers=1)


if __name__ == '__main__':
    main()
