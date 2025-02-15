from typing import Generic, TypeVar, Type

from pydantic import BaseModel
from sqlalchemy import Row, RowMapping

from src.infrastructure.db.models.base import Base


ModelType = TypeVar("ModelType", bound=Base)
SchemaType = TypeVar("SchemaType", bound=BaseModel)


class BaseMapper(Generic[ModelType, SchemaType]):
    model: Type[ModelType]
    schema: Type[SchemaType]

    @classmethod
    def from_orm(cls, data: Type[ModelType] | ModelType | dict | Row | RowMapping) -> SchemaType:
        return cls.schema.model_validate(data, from_attributes=True)

    @classmethod
    def to_orm(cls, data: BaseModel) -> Type[ModelType]:
        return cls.model(**data.model_dump())

    @classmethod
    def to_orm_exclude_unset(cls, data: BaseModel) -> Type[ModelType]:
        return cls.model(**data.model_dump(exclude_unset=True))

    @classmethod
    def to_dict(cls, data: BaseModel) -> dict:
        return data.model_dump()

    @classmethod
    def to_dict_exclude_unset(cls, data: BaseModel) -> dict:
        return data.model_dump(exclude_unset=True)
