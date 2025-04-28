from functools import partial
from anyio.to_thread import run_sync
from typing import TypedDict

from didiator import Command, CommandHandler
from google.oauth2 import id_token
from google.auth.transport import requests
from google.auth.exceptions import GoogleAuthError

from src.application.auth.dto import GoogleAuthDTO, InsertUserDTO
from src.application.auth.interfaces import AuthRepo, AuthReader
from src.infrastructure.db.uow import UnitOfWork
from src.application.common.exceptions.auth import GoogleAuthorizationError


class GoogleAuthTokenData(TypedDict):
    iss: str
    azp: str
    aud: str
    sub: str
    email: str
    email_verified: bool
    nbf: int
    name: str
    picture: str
    given_name: str
    family_name: str
    iat: int
    exp: int
    jti: str


class GoogleAuth(GoogleAuthDTO, Command[int]):
    pass


class GoogleAuthHandler(CommandHandler[GoogleAuth, int]):
    def __init__(self, repo: AuthRepo, reader: AuthReader, uow: UnitOfWork):
        self.repo = repo
        self.reader = reader
        self.uow = uow

    async def __call__(self, command: GoogleAuth) -> int:
        func = partial(
            id_token.verify_token,
            id_token=command.credential,
            request=requests.Request(),
            clock_skew_in_seconds=5
        )

        try:
            user_data: GoogleAuthTokenData = await run_sync(func)
            print(user_data)
        except GoogleAuthError:
            raise GoogleAuthorizationError

        user = await self.reader.select_by_email(user_data["email"])

        if user is None:
            insert_user = InsertUserDTO(
                name=user_data["name"],
                email=user_data["email"],
                avatar_url=user_data["picture"],
                hashed_password=None
            )

            user = await self.repo.insert_one(insert_user)
            await self.uow.commit()

        return user.id
