from didiator import Mediator

from src.application.auth.commands.register_user import RegisterUser, RegisterUserHandler
from src.application.auth.commands.google_auth import GoogleAuth, GoogleAuthHandler
from src.application.auth.queries.login_user import LoginUser, LoginUserHandler


def setup_auth_handlers(mediator: Mediator):
    mediator.register_command_handler(RegisterUser, RegisterUserHandler)
    mediator.register_command_handler(GoogleAuth, GoogleAuthHandler)

    mediator.register_query_handler(LoginUser, LoginUserHandler)
