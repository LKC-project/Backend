from typing import Protocol
from hashlib import sha256

from aiobotocore.client import AioBaseClient

from src.infrastructure.s3.s3_client import S3ClientConfig


class ObjectStorage(Protocol):
    def __init__(self, s3: AioBaseClient, config: S3ClientConfig):
        self.s3 = s3
        self.config = config

    def gen_url(self, object_name: str) -> str:
        ...

    async def put_object(self, obj: bytes, name: str | None = None) -> str:
        ...


class ObjectStorageImpl(ObjectStorage):
    @staticmethod
    def _gen_object_hash(obj: bytes) -> str:
        return sha256(obj).hexdigest()[:12]

    def gen_url(self, object_name: str) -> str:
        return self.config.endpoint_url.replace(
            "://", "://{}."
        ).format(self.config.bucket_name) + f"/{object_name}"

    async def put_object(self, obj: bytes, name: str | None = None) -> str:
        object_name = name or self._gen_object_hash(obj)

        await self.s3.put_object(
            Bucket=self.config.bucket_name,
            Key=object_name,
            Body=obj
        )

        return self.gen_url(object_name)
