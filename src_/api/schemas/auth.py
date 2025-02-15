from pydantic import BaseModel, Field


class SLoginRequest(BaseModel):
    name: str = Field(max_length=48)
    password: str = Field(max_length=256)
