from fastapi import APIRouter
from app.service.user_service.user_handle import router as user_user_handle_router
from app.service.user_service.auth_handle import router as user_auth_handle_router

user_router = APIRouter()
user_router.include_router(user_user_handle_router)
user_router.include_router(user_auth_handle_router)
