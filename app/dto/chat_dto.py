# -*- coding: utf-8 -*-
from pydantic import BaseModel, Field


class ChatHistory(BaseModel):
    role: str = Field(..., description='chat role,example:AI,USER')
    content: str = Field(..., description='chat content')
