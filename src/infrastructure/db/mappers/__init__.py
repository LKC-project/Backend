from src.infrastructure.db.mappers.base import BaseMapper
from src.infrastructure.db.models.user import UserORM
from src.application.user.dto import UserDTO


class UserMapper(BaseMapper[UserORM, UserDTO]):
    model = UserORM
    schema = UserDTO
