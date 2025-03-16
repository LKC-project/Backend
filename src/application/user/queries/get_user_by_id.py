from didiator import Query, QueryHandler

from src.application.common.dto import DTO
from src.application.user.dto import UserDTO
from src.application.user.interfaces import UserReader


class GetUserByID(DTO, Query[UserDTO]):
    id: int


class GetUserByIDHandler(QueryHandler[GetUserByID, UserDTO]):
    def __init__(self, reader: UserReader):
        self.reader = reader

    async def __call__(self, command: GetUserByID) -> UserDTO | None:
        return await self.reader.select_by_id(command.id)
