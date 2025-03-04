from typing import AsyncGenerator

from aiobotocore.session import get_session
from aiobotocore.client import AioBaseClient

from src.infrastructure.s3.config import S3ClientConfig


async def get_s3_client(config: S3ClientConfig) -> AsyncGenerator[AioBaseClient, None]:
    async with get_session().create_client("s3", **config.client_config) as client:
        yield client
