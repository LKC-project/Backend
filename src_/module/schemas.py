from pydantic import BaseModel, Field


class SModule(BaseModel):
    id: int
    name: str = Field(max_length=48)
    description: str = Field(max_length=256)


class SModuleFilters(BaseModel):
    id: int | None = Field(default=None)
    name: str | None = Field(default=None, max_length=48)
    description: str | None = Field(default=None, max_length=256)


class SModulePOST(BaseModel):
    name: str = Field(max_length=48)
    description: str = Field(max_length=256)
