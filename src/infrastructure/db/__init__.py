from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker, AsyncEngine

from src.config import config


async def build_sa_engine() -> AsyncGenerator[AsyncEngine, None]:  # TODO: Config dep.
    engine = create_async_engine(config.db_url)

    yield engine

    await engine.dispose()


def build_async_session_maker(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)


async def get_async_session(
        async_session_maker: async_sessionmaker[AsyncSession]
) -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
