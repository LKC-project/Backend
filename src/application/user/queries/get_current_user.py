from didiator import Query, QueryHandler

from src.application.common.dto import DTO
from src.application.user.dto import UserDTO
from src.application.user.interfaces import UserReader
from src.application.common.exceptions.auth import Unauthorized


class GetCurrentUser(DTO, Query[UserDTO]):
    id: int


class GetCurrentUserHandler(QueryHandler[GetCurrentUser, UserDTO]):
    def __init__(self, reader: UserReader):
        self.reader = reader

    async def __call__(self, command: GetCurrentUser) -> UserDTO:
        user = await self.reader.select_by_id(command.id)

        if user is None:
            raise Unauthorized

        return user
