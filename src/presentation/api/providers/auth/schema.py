from abc import ABCMeta, abstractmethod
from typing import Any

from fastapi import Request
from fastapi.security.api_key import APIKeyCookie

from src.application.common.exceptions.auth import Unauthorized

from src.presentation.api.providers.auth.transport import Transport
from src.presentation.api.providers.auth.strategy import Strategy


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
        pass


class CurrentUserID(BaseSecuritySchema):
    async def __call__(self, request: Request) -> int | None:
        token = self.transport.read(request)

        if token is None:
            if self.auto_error:
                raise Unauthorized
            return None

        data = self.strategy.decode(token)

        return data["id"]
