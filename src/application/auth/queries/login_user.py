from didiator import Query, QueryHandler

from src.application.auth.dto import LoginUserDTO
from src.application.auth.interfaces import AuthReader
from src.application.common.exceptions.auth import WrongEmailOrPassword

from src.application.auth.password import Password


class LoginUser(LoginUserDTO, Query[int]):
    pass


class LoginUserHandler(QueryHandler[LoginUser, int]):
    def __init__(self, reader: AuthReader):
        self.reader = reader

    async def __call__(self, command: LoginUser) -> int:
        user = await self.reader.select_by_email(command.email)

        if user is None:
            raise WrongEmailOrPassword

        if user.hashed_password is None:
            raise WrongEmailOrPassword

        if not Password.valid(command.password, user.hashed_password):
            raise WrongEmailOrPassword

        return user.id
