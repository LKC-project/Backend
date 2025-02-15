from didiator import Query, QueryHandler

from src.application.auth.dto import LoginUserDTO
from src.application.auth.interfaces import AuthReader
from src.application.common.exceptions.auth import WrongLoginOrPassword

from src.application.auth.password import Password
from src.application.auth.token import Token


class LoginUser(LoginUserDTO, Query[str]):
    pass


class LoginUserHandler(QueryHandler[LoginUser, str]):
    def __init__(self, reader: AuthReader):
        self.reader = reader

    async def __call__(self, command: LoginUser) -> str:
        user = await self.reader.select_by_name(command.name)

        if user is None:
            raise WrongLoginOrPassword

        if not Password.valid(command.password, user.hashed_password):
            raise WrongLoginOrPassword

        token = Token.encode({"id": user.id})

        return token
