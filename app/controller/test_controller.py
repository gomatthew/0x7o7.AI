from fastapi import APIRouter

router = APIRouter(
    prefix='/test',
    tags=['test'],
    responses={200: {'description': 'success'}}
)


@router.get('/test1')
async def test_func():
    return {"status": 200}
