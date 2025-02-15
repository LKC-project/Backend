from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.common.exceptions.unexpected import CommitError, RollbackError
from src.application.common.interfaces.uow import UnitOfWork


def build_uow(session: AsyncSession) -> UnitOfWork:
    return SQLAlchemyUoW(session=session)


class SQLAlchemyUoW(UnitOfWork):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def commit(self) -> None:
        try:
            await self.session.commit()
        except SQLAlchemyError as err:
            raise CommitError from err

    async def rollback(self) -> None:
        try:
            await self.session.rollback()
        except SQLAlchemyError as err:
            raise RollbackError from err
