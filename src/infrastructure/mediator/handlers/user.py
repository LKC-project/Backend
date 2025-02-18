from didiator import Mediator

from src.application.user.queries.get_user_by_id import GetUserByID, GetUserByIDHandler


def setup_user_handlers(mediator: Mediator):
    mediator.register_query_handler(GetUserByID, GetUserByIDHandler)
