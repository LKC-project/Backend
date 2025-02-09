from fastapi import Response

from src.services.auth.transport import CookieTransport
from src.services.auth.strategy import JWTStrategy

from src.services.auth.schema import CurrentUserID

from src.config import settings


class AuthService:
    def __init__(self, name: str = "access_token"):
        self.name = name

        self.transport = CookieTransport(name=self.name)
        self.strategy = JWTStrategy(secret=settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

        self.current_user_id = CurrentUserID(self.transport, self.strategy, self.name)
        self.current_user_id_or_none = CurrentUserID(self.transport, self.strategy, self.name, auto_error=False)
        self.current_user = ...
        self.current_admin = ...

    def login(self, user_id: int, response: Response = Response()) -> Response:
        token = self.strategy.encode({"id": user_id})
        response = self.transport.write(token, response)

        return response

    def logout(self, response: Response = Response()) -> Response:
        return self.transport.delete(response)
