from fastapi import APIRouter

test_router = APIRouter(
    prefix='/test',
    tags=['test'],
    responses={200: {'description': 'success'}}
)



