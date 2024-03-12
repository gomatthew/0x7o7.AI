from fastapi import FastAPI
from app.controller import test_router

def create_app():
    app = FastAPI()
    app.include_router(test_router)
    return app
app = create_app()