from pydantic import BaseModel


class CounterDTO(BaseModel):
    id: int
    value: int
