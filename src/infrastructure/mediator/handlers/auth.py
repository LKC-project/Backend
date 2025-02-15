from didiator import Mediator

from src.application.auth.commands.login_user import UserLogin, UserLoginHandler


def setup_auth_handlers(mediator: Mediator):
    mediator.register_command_handler(UserLogin, UserLoginHandler)
