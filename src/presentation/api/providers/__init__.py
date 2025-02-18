from di import ScopeState
from didiator import CommandMediator, EventMediator, Mediator, QueryMediator
from didiator.interface.utils.di_builder import DiBuilder
from fastapi import FastAPI

from src.presentation.api.providers.di import StateProvider, get_di_builder, get_di_state
from src.presentation.api.providers.mediator import MediatorProvider
from src.presentation.api.providers.stub import Stub


def setup_providers(
    app: FastAPI,
    mediator: Mediator,  # noqa
    di_builder: DiBuilder,
    di_state: ScopeState | None = None,
) -> None:
    mediator_provider = MediatorProvider(mediator)

    app.dependency_overrides[Stub(Mediator)] = mediator_provider.build  # noqa: не ми такі, життя таке
    app.dependency_overrides[Stub(CommandMediator)] = mediator_provider.build  # noqa: не ми такі, життя таке
    app.dependency_overrides[Stub(QueryMediator)] = mediator_provider.build  # noqa: не ми такі, життя таке
    app.dependency_overrides[Stub(EventMediator)] = mediator_provider.build  # noqa: не ми такі, життя таке

    state_provider = StateProvider(di_state)

    app.dependency_overrides[get_di_builder] = lambda: di_builder  # noqa: не ми такі, життя таке
    app.dependency_overrides[get_di_state] = state_provider.build  # noqa: не ми такі, життя таке
