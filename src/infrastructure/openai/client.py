from typing import Protocol, AsyncGenerator

from openai import AsyncOpenAI

from src.infrastructure.openai.config import OpenAIClientConfig


class OpenAIClient(Protocol):
    async def send_prompt(self, prompt: str, context: list[dict] = None) -> str:
        ...


class OpenAIClientImpl(AsyncOpenAI, OpenAIClient):
    def __init__(self, config: OpenAIClientConfig):
        super().__init__(api_key=config.api_key, base_url="https://api.deepseek.com")

    async def send_prompt(self, prompt: str, context: list[dict] = None) -> str:
        context = (context or []).copy()

        context.append({"role": "user", "content": prompt})

        response = await self.chat.completions.create(
            model="deepseek-chat",
            messages=context,
            stream=False
        )

        return response.choices[0].message.content


async def get_openai_client(config: OpenAIClientConfig) -> AsyncGenerator[OpenAIClient, None]:
    client = OpenAIClientImpl(config)

    yield client

    await client.close()
