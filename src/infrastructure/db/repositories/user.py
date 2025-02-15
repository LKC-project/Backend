from sqlalchemy import insert, select

from src.infrastructure.db.repositories.base import BaseRepo
from src.infrastructure.db.models.user import UserORM
from src.infrastructure.db.mappers import UserMapper
from src.application.user.interfaces import UserReader, UserRepo
from src.application.user.dto import UserDTO, UserCreateDTO, UserWithPasswordDTO


class UserReaderImpl(BaseRepo[UserORM], UserReader):
    model = UserORM
    mapper = UserMapper

    async def select_by_id(self, id: int) -> UserDTO | None:
        user = await self.session.get(self.model, id)

        return None if user is None else self.mapper.from_orm(user)

    async def select_by_name(self, name: str) -> UserDTO | None:
        query = (
            select(self.model)
            .where(self.model.name.ilike(name))
        )

        result = await self.session.scalar(query)

        return None if result is None else self.mapper.from_orm(result)

    async def select_with_password_by_name(self, name: str) -> UserWithPasswordDTO | None:
        query = (
            select(self.model)
            .where(self.model.name.ilike(name))
        )

        result = await self.session.scalar(query)

        return None if result is None else UserWithPasswordDTO.model_validate(
            result, from_attributes=True
        )  # TODO: Mapper


class UserRepoImpl(BaseRepo[UserORM], UserRepo):
    model = UserORM
    mapper = UserMapper

    async def insert_one(self, user: UserCreateDTO) -> UserDTO:
        stmt = (
            insert(self.model)
            .values(**self.mapper.to_dict(user))
            .returning(self.model)
        )

        result = await self.session.scalar(stmt)

        return self.mapper.from_orm(result)
