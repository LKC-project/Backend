from src.infrastructure.db.mappers.base import BaseMapper
from src.infrastructure.db.models.user import UserORM
from src.application.user.dto import UserDTO
from src.application.auth.dto import UserDTO as AuthUserDTO


class UserMapper(BaseMapper[UserORM, UserDTO]):
    model = UserORM
    schema = UserDTO


class AuthMapper(BaseMapper[UserORM, AuthUserDTO]):
    model = UserORM
    schema = AuthUserDTO
