from typing import Callable

from di import Container, bind_by_type
from di.dependent import Dependent
from di.executors import AsyncExecutor

from didiator import Mediator, QueryMediator, CommandMediator
from didiator.utils.di_builder import DiBuilderImpl
from didiator.interface.utils.di_builder import DiBuilder

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, AsyncEngine

from src.infrastructure.mediator import get_mediator
from src.infrastructure.di.constants import DiScope
from src.infrastructure.db import get_async_session, build_async_session_maker, build_sa_engine
from src.infrastructure.db.uow import build_uow
from src.application.common.interfaces.uow import UnitOfWork
from src.application.user.interfaces import UserReader, UserRepo
from src.infrastructure.db.repositories.user import UserReaderImpl, UserRepoImpl


def init_di_builder() -> DiBuilder:
    di_container = Container()
    di_executor = AsyncExecutor()
    di_scopes = [DiScope.APP, DiScope.REQUEST]
    di_builder = DiBuilderImpl(
        di_container=di_container,
        di_executor=di_executor,
        di_scopes=di_scopes
    )

    return di_builder


def setup_di_builder(di_builder: DiBuilder) -> None:
    di_builder.bind(bind_by_type(Dependent(lambda *args: di_builder, scope=DiScope.APP), DiBuilder))
    di_builder.bind(bind_by_type(Dependent(build_uow, scope=DiScope.REQUEST), UnitOfWork))
    setup_mediator_factory(di_builder, get_mediator, DiScope.REQUEST)
    setup_db_factories(di_builder)


def setup_mediator_factory(
    di_builder: DiBuilder,
    mediator_factory: Callable,
    scope: DiScope,
):
    di_builder.bind(bind_by_type(Dependent(mediator_factory, scope=scope), Mediator))
    di_builder.bind(bind_by_type(Dependent(mediator_factory, scope=scope), QueryMediator))
    di_builder.bind(bind_by_type(Dependent(mediator_factory, scope=scope), CommandMediator))


def setup_db_factories(di_builder: DiBuilder):
    di_builder.bind(bind_by_type(Dependent(build_sa_engine, scope=DiScope.APP), AsyncEngine, covariant=True))
    di_builder.bind(
        bind_by_type(
            Dependent(build_async_session_maker, scope=DiScope.APP),
            async_sessionmaker[AsyncSession]
        )
    )
    di_builder.bind(bind_by_type(Dependent(get_async_session, scope=DiScope.REQUEST), AsyncSession, covariant=True))

    di_builder.bind(bind_by_type(Dependent(UserReaderImpl, scope=DiScope.REQUEST), UserReader, covariant=True))
    di_builder.bind(bind_by_type(Dependent(UserRepoImpl, scope=DiScope.REQUEST), UserRepo, covariant=True))
