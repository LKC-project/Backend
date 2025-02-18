from didiator import Query, QueryHandler

from src.application.auth.dto import UserDTO, SelectUserByIDDTO
from src.application.auth.interfaces import AuthReader


class GetUserByID(SelectUserByIDDTO, Query[UserDTO]):
    pass


class GetUserByIDHandler(QueryHandler[GetUserByID, UserDTO]):
    def __init__(self, reader: AuthReader):
        self.reader = reader

    async def __call__(self, command: GetUserByID) -> UserDTO | None:
        user = await self.reader.select_by_id(command.id)

        return user
