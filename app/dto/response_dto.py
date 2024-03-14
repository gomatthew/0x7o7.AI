import pydantic
from pydantic import BaseModel
from typing import Any


class BaseResponse(BaseModel):
    status: int = pydantic.Field(..., description='status code')
    message: str = pydantic.Field(..., description='return message')
    data: Any = pydantic.Field(None, description='service return data')

    class Config:
        json_schema_extra = {
            "example": {
                "status": 200,
                "message": "success",
                "data": {"field": "value"},
            }
        }


class ResponseHttp200(BaseResponse):
    status: int = pydantic.Field(200, description='status code')
    message: str = pydantic.Field(200, description='return message')
    data: Any = pydantic.Field(..., description='json status')
