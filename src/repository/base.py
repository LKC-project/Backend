from typing import Type, TypeVar, Generic, Sequence

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import Base


ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    model: Type[ModelType]

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_one(self, **filter_by) -> ModelType:
        query = (
            select(self.model)
            .filter_by(**filter_by)
        )

        response = await self.session.execute(query)

        return response.scalars().one_or_none()

    async def insert_one(self, **values) -> ModelType:
        query = (
            insert(self.model)
            .values(**values)
            .returning(self.model)
        )

        response = await self.session.execute(query)

        return response.scalars().one()

    async def get_many(self, limit: int | None = None, offset: int | None = None, **filter_by) -> Sequence[ModelType]:
        query = (
            select(self.model)
            .filter_by(**filter_by)
        )

        if limit:
            query = query.limit(limit)

        if offset:
            query = query.offset(offset)

        response = await self.session.execute(query)

        return response.scalars().all()

    async def insert_many(self, values: Sequence[dict]) -> Sequence[ModelType]:
        query = (
            insert(self.model)
            .returning(self.model)
        )

        response = await self.session.execute(query, values)

        return response.scalars().all()
