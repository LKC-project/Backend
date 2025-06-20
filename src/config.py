from os import getenv

from pydantic_settings import BaseSettings, SettingsConfigDict


env = str(getenv("ENV")).lower()
env_file = ".env"


if env == "dev":
    env_file = ".env-dev"
elif env == "test":
    env_file = ".env-test"


class Config(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    AWS_S3_ACCESS_KEY: str
    AWS_S3_SECRET_KEY: str
    AWS_S3_ENDPOINT_URL: str
    AWS_S3_BUCKET_NAME: str

    JWT_SECRET: str
    JWT_ALGORITHM: str

    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str

    OPEN_AI_TOKEN: str

    model_config = SettingsConfigDict(env_file=env_file)

    @property
    def db_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


config = Config()
