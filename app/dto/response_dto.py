import pydantic
from pydantic import BaseModel
from typing import Any


class BaseResponse(BaseModel):
    status: int = pydantic.Field(..., description='status code')
    message: str = pydantic.Field(..., description='return message')
    data: Any = pydantic.Field(None, description='service return data')

    class Config:
        schema_extra = {
            "example": {
                "status": 200,
                "message": "success",
                "data": {"field": "value"},
            }
        }


class ResponseHttp200(BaseResponse):
    status = 200
    message = 'success'
    data = None
