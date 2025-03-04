from dataclasses import dataclass

from src.config import Config


@dataclass(frozen=True)
class S3ClientConfig:
    access_key: str
    secret_key: str
    endpoint_url: str
    bucket_name: str

    @property
    def client_config(self):
        return {
            "aws_access_key_id": self.access_key,
            "aws_secret_access_key": self.secret_key,
            "endpoint_url": self.endpoint_url
        }


def setup_s3_config(config: Config) -> S3ClientConfig:
    return S3ClientConfig(
        access_key=config.AWS_S3_ACCESS_KEY,
        secret_key=config.AWS_S3_SECRET_KEY,
        endpoint_url=config.AWS_S3_ENDPOINT_URL,
        bucket_name=config.AWS_S3_BUCKET_NAME
    )

