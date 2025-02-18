from fastapi import Response

from src.presentation.api.providers.auth.transport import CookieTransport
from src.presentation.api.providers.auth.strategy import JWTStrategy

from src.presentation.api.providers.auth.schema import CurrentUserID

from src.config import config


class AuthProviderConfig:
    JWT_SECRET: str
    JWT_ALGORITHM: str


class AuthProvider:
    def __init__(self, name: str = "access_token"):
        self.name = name

        self.transport = CookieTransport(name=self.name)
        self.strategy = JWTStrategy(secret=config.JWT_SECRET, algorithm=config.JWT_ALGORITHM)

        self.current_user_id = CurrentUserID(self.transport, self.strategy, self.name)
        self.current_user_id_or_none = CurrentUserID(self.transport, self.strategy, self.name, auto_error=False)

    def login(self, user_id: int, response: Response = Response()) -> Response:
        token = self.strategy.encode({"id": user_id})
        response = self.transport.write(token, response)

        return response

    def logout(self, response: Response = Response()) -> Response:
        return self.transport.delete(response)


auth_provider = AuthProvider()
