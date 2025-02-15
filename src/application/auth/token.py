from jwt import encode, decode
from jwt.exceptions import InvalidSignatureError

from src.application.common.exceptions.auth import InvalidToken


SECRET = "sd"
ALGORITHM = "HS256"


class Token:
    @staticmethod
    def encode(data: dict) -> str:
        return encode(
            payload=data,
            key=SECRET,
            algorithm=ALGORITHM
        )

    @staticmethod
    def decode(token: str) -> dict:
        try:
            return decode(
                jwt=token,
                key=SECRET,
                algorithms=[ALGORITHM]
            )
        except InvalidSignatureError:
            raise InvalidToken
