from abc import ABCMeta, abstractmethod

from jwt import encode, decode
from jwt.exceptions import InvalidSignatureError

from src_.services.auth.etc import AuthData
from src_.services.auth.exceptions import NotAuthenticatedException


class Strategy(metaclass=ABCMeta):
    def __init__(self, secret: str, algorithm: str = "HS256"):
        self.secret = secret
        self.algorithm = algorithm

    @abstractmethod
    def encode(self, data: dict) -> str:
        ...

    @abstractmethod
    def decode(self, token: str) -> AuthData:
        ...


class JWTStrategy(Strategy):
    def encode(self, data: AuthData) -> str:
        return encode(
            payload=data,
            key=self.secret,
            algorithm=self.algorithm
        )

    def decode(self, token: str) -> AuthData:
        try:
            return decode(
                jwt=token,
                key=self.secret,
                algorithms=[self.algorithm]
            )
        except InvalidSignatureError:
            raise NotAuthenticatedException
