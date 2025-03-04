from typing import Generic, TypeVar, Type

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.db.mappers.base import BaseMapper


Model = TypeVar("Model", bound=DeclarativeBase)


class BaseRepo(Generic[Model]):  # TODO: Mapper generic
    model: Type[Model]
    mapper: Type[BaseMapper]

    def __init__(self, session: AsyncSession):
        self.session = session
