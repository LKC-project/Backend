from dataclasses import dataclass

from src.config import Config


@dataclass(frozen=True)
class OpenAIClientConfig:
    api_key: str


def setup_openai_config(config: Config) -> OpenAIClientConfig:
    return OpenAIClientConfig(
        api_key=config.OPEN_AI_TOKEN
    )

