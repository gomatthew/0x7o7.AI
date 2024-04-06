# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI
# from service import *
from test.service import router
# @router.post('/tag1')
# async def foo():
#     return 'hello world'

app = FastAPI()
app.include_router(router)


uvicorn.run(app=app)
