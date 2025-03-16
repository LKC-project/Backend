from sqlalchemy import insert, select
from sqlalchemy.exc import IntegrityError

from src.infrastructure.db.repositories.base import BaseRepo
from src.infrastructure.db.models.user import UserORM
from src.infrastructure.db.mappers import AuthMapper
from src.application.auth.interfaces import AuthReader, AuthRepo
from src.application.auth.dto import UserDTO, InsertUserDTO
from src.application.common.exceptions.auth import EmailAlreadyInUse


class AuthReaderImpl(BaseRepo[UserORM], AuthReader):
    model = UserORM
    mapper = AuthMapper

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

    async def select_by_email(self, email: str) -> UserDTO | None:
        query = (
            select(self.model)
            .where(self.model.email.ilike(email))
        )

        result = await self.session.scalar(query)

        return None if result is None else self.mapper.from_orm(result)


class AuthRepoImpl(BaseRepo[UserORM], AuthRepo):
    model = UserORM
    mapper = AuthMapper

    @staticmethod
    def _parse_error(err: IntegrityError):
        match getattr(err.orig.__cause__, "constraint_name"):
            case "ix_User_email":
                raise EmailAlreadyInUse

    async def insert_one(self, user: InsertUserDTO) -> UserDTO:
        stmt = (
            insert(self.model)
            .values(**self.mapper.to_dict(user))
            .returning(self.model)
        )

        try:
            result = await self.session.scalar(stmt)
            return self.mapper.from_orm(result)
        except IntegrityError as err:
            self._parse_error(err)
