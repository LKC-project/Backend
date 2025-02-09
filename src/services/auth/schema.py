from abc import ABCMeta, abstractmethod
from typing import Any

from fastapi import Request
from fastapi.security.api_key import APIKeyCookie

from src.services.auth.transport import Transport
from src.services.auth.strategy import Strategy
from src.services.auth.exceptions import NotAuthenticatedException


class BaseSecuritySchema(APIKeyCookie, metaclass=ABCMeta):
    def __init__(
            self,
            transport: Transport,
            strategy: Strategy,
            name: str,
            scheme_name: str | None = None,
            description: str | None = None,
            auto_error: bool = True,
    ):
        super().__init__(name=name, scheme_name=scheme_name, description=description, auto_error=auto_error)

        self.transport = transport
        self.strategy = strategy

    @abstractmethod
    async def __call__(self, request: Request) -> Any:
        ...


class CurrentUserID(BaseSecuritySchema):
    async def __call__(self, request: Request) -> int | None:
        token = self.transport.read(request)

        if token is None:
            if self.auto_error:
                raise NotAuthenticatedException
            return None

        data = self.strategy.decode(token)

        return data["id"]


class CurrentUser(BaseSecuritySchema):
    async def __call__(self, request: Request) -> str | None:
        raise NotImplemented
