from src.infrastructure.db.mappers.base import BaseMapper
from src.infrastructure.db.models.user import UserORM
from src.infrastructure.db.models.project import ProjectORM
from src.application.user.dto import UserDTO
from src.application.auth.dto import UserDTO as AuthUserDTO
from src.application.project.dto import ProjectDTO


class UserMapper(BaseMapper[UserORM, UserDTO]):
    model = UserORM
    schema = UserDTO


class AuthMapper(BaseMapper[UserORM, AuthUserDTO]):
    model = UserORM
    schema = AuthUserDTO


class ProjectMapper(BaseMapper[ProjectORM, ProjectDTO]):
    model = ProjectORM
    schema = ProjectDTO
