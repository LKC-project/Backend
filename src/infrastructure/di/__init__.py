from typing import Callable

from di import Container, bind_by_type
from di.dependent import Dependent
from di.executors import AsyncExecutor

from didiator import Mediator, QueryMediator, CommandMediator
from didiator.utils.di_builder import DiBuilderImpl
from didiator.interface.utils.di_builder import DiBuilder

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, AsyncEngine
from aiobotocore.client import AioBaseClient

from src.config import Config
from src.infrastructure.mediator import get_mediator
from src.infrastructure.di.constants import DiScope
from src.infrastructure.db import get_async_session, build_async_session_maker, build_sa_engine
from src.infrastructure.db.uow import build_uow
from src.application.common.interfaces.uow import UnitOfWork
from src.application.user.interfaces import UserReader, UserRepo
from src.infrastructure.db.repositories.user import UserReaderImpl, UserRepoImpl
from src.application.auth.interfaces import AuthReader, AuthRepo
from src.infrastructure.db.repositories.auth import AuthReaderImpl, AuthRepoImpl
from src.application.project.interfaces import ProjectReader, ProjectRepo
from src.infrastructure.db.repositories.project import ProjectReaderImpl, ProjectRepoImpl
from src.infrastructure.s3 import ObjectStorage, ObjectStorageImpl, S3ClientConfig, get_s3_client, setup_s3_config
from src.infrastructure.openai import OpenAIClient, OpenAIClientConfig, get_openai_client, setup_openai_config


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

    setup_mediator_factories(di_builder, get_mediator, DiScope.REQUEST)
    setup_db_factories(di_builder)
    setup_s3_factory(di_builder)
    setup_clients(di_builder)


def setup_mediator_factories(
    di_builder: DiBuilder,
    mediator_factory: Callable,
    scope: DiScope,
):
    di_builder.bind(bind_by_type(Dependent(mediator_factory, scope=scope), Mediator))
    di_builder.bind(bind_by_type(Dependent(mediator_factory, scope=scope), QueryMediator))
    di_builder.bind(bind_by_type(Dependent(mediator_factory, scope=scope), CommandMediator))


def setup_config_factories(di_builder: DiBuilder, config: Config):
    di_builder.bind(bind_by_type(Dependent(lambda: config, scope=DiScope.APP), Config))
    di_builder.bind(bind_by_type(Dependent(setup_s3_config, scope=DiScope.APP), S3ClientConfig))
    di_builder.bind(bind_by_type(Dependent(setup_openai_config, scope=DiScope.APP), OpenAIClientConfig))


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

    di_builder.bind(bind_by_type(Dependent(AuthReaderImpl, scope=DiScope.REQUEST), AuthReader, covariant=True))
    di_builder.bind(bind_by_type(Dependent(AuthRepoImpl, scope=DiScope.REQUEST), AuthRepo, covariant=True))

    di_builder.bind(bind_by_type(Dependent(ProjectReaderImpl, scope=DiScope.REQUEST), ProjectReader, covariant=True))
    di_builder.bind(bind_by_type(Dependent(ProjectRepoImpl, scope=DiScope.REQUEST), ProjectRepo, covariant=True))


def setup_s3_factory(di_builder: DiBuilder):
    di_builder.bind(bind_by_type(Dependent(get_s3_client, scope=DiScope.REQUEST), AioBaseClient, covariant=True))
    di_builder.bind(bind_by_type(Dependent(ObjectStorageImpl, scope=DiScope.REQUEST), ObjectStorage, covariant=True))


def setup_clients(di_builder: DiBuilder):
    di_builder.bind(bind_by_type(Dependent(get_openai_client, scope=DiScope.REQUEST), OpenAIClient))
