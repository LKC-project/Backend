from didiator import Mediator

from src.application.user.commands.create_user import UserCreateHandler, UserCreate


def setup_user_handlers(mediator: Mediator):
    mediator.register_command_handler(UserCreate, UserCreateHandler)
