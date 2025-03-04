from didiator import Mediator, MediatorImpl, QueryDispatcherImpl, CommandDispatcherImpl, EventObserverImpl
from didiator.middlewares.di import DiMiddleware, DiScopes
from didiator.interface.utils.di_builder import DiBuilder

from src.infrastructure.di.constants import DiScope
from src.infrastructure.mediator.handlers.user import setup_user_handlers
from src.infrastructure.mediator.handlers.auth import setup_auth_handlers
from src.infrastructure.mediator.handlers.image import setup_image_handlers
from src.infrastructure.mediator.handlers.project import setup_project_handlers


def get_mediator() -> Mediator:
    raise NotImplementedError


def init_mediator(di_builder: DiBuilder) -> Mediator:
    middlewares = (
        DiMiddleware(di_builder, scopes=DiScopes(DiScope.REQUEST)),
    )

    command_dispatcher = CommandDispatcherImpl(middlewares=middlewares)
    query_dispatcher = QueryDispatcherImpl(middlewares=middlewares)
    event_observer = EventObserverImpl(middlewares=middlewares)

    mediator = MediatorImpl(command_dispatcher, query_dispatcher, event_observer)

    return mediator


def setup_mediator(mediator: Mediator):
    setup_user_handlers(mediator)
    setup_auth_handlers(mediator)
    setup_image_handlers(mediator)
    setup_project_handlers(mediator)
