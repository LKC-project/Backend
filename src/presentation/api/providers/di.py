from typing import Annotated
from collections.abc import AsyncGenerator

from di import ScopeState
from didiator.interface.utils.di_builder import DiBuilder
from fastapi import Depends

from src.infrastructure.di import DiScope


def get_di_builder() -> DiBuilder:
    raise NotImplementedError


def get_di_state() -> ScopeState:
    raise NotImplementedError


class StateProvider:
    def __init__(self, di_state: ScopeState | None = None) -> None:
        self.di_state = di_state

    async def build(
            self,
            di_builder: Annotated[DiBuilder, Depends(get_di_builder)]
    ) -> AsyncGenerator[ScopeState, None]:
        async with di_builder.enter_scope(DiScope.REQUEST, self.di_state) as di_state:
            yield di_state
