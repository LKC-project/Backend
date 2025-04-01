from abc import ABCMeta, abstractmethod

from fastapi import Request, Response


class Transport(metaclass=ABCMeta):
    def __init__(self, name: str, expires: int = 36000000):
        self.name = name
        self.expires = expires

    @abstractmethod
    def write(self, token: str, response: Response = Response()) -> Response:
        pass

    @abstractmethod
    def read(self, request: Request) -> str | None:
        ...

    @abstractmethod
    def delete(self) -> Response:
        ...


class CookieTransport(Transport):
    def write(self, token: str, response: Response = Response()) -> Response:
        response.set_cookie(
            key=self.name,
            value=token,
            expires=self.expires,
            samesite="none",
            secure=True,
        )

        return response

    def read(self, request: Request) -> str | None:
        return request.cookies.get(self.name)

    def delete(self, response: Response = Response()) -> Response:
        response.delete_cookie(
            key=self.name,
            samesite="none",
            secure=True,
        )

        return response
