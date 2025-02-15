from fastapi import HTTPException, status  # TODO: !!!!!!!!!!!! GOVNOCODE !!!!!!!!!!!!
from didiator import Command, CommandHandler
from jwt import decode, encode
from jwt.exceptions import InvalidSignatureError

from src.application.auth.dto import UserLoginDTO
from src.application.user.interfaces import UserReader


class JWTStrategy:
    @staticmethod
    def encode(id: int) -> str:
        return encode(
            payload={"id": id},
            key="Bruh",
            algorithm="HS256"
        )

    @staticmethod
    def decode(token: str) -> dict:
        try:
            return decode(
                jwt=token,
                key="Bruh",
                algorithms=["HS256"]
            )
        except InvalidSignatureError:
            raise HTTPException(
                detail="Not unauthorized",
                status_code=status.HTTP_401_UNAUTHORIZED
            )


class UserLogin(UserLoginDTO, Command[str]):
    pass


class UserLoginHandler(CommandHandler[UserLogin, str]):
    def __init__(self, reader: UserReader):
        self.reader = reader

    async def __call__(self, command: UserLogin) -> str:
        user = await self.reader.select_with_password_by_name(command.name)

        print(user.password, command.password)

        if user.password != command.password:
            raise HTTPException(
                detail="Wrong login or password",
                status_code=status.HTTP_401_UNAUTHORIZED
            )

        token = JWTStrategy.encode(user.id)

        return token
