from didiator import Command, CommandHandler

from src.application.common.dto import DTO
from src.application.chat.enums import MessageRole
from src.application.chat.dto import SendPromptDTO, ResponseDTO
from src.infrastructure.openai import OpenAIClient


class SendPrompt(DTO, Command[ResponseDTO]):
    project_id: int
    prompt: SendPromptDTO


class SendPromptHandler(CommandHandler[SendPrompt, ResponseDTO]):
    def __init__(self, client: OpenAIClient):
        self.client = client

    async def __call__(self, command: SendPrompt) -> ResponseDTO | None:
        context = []

        for item in command.prompt.context:
            context.append({"role": "user", "content": f"NOTE {item.name}: {item.content}"})

        for item in command.prompt.history:
            context.append({"role": "user" if item.role == MessageRole.USER else "system", "content": item.content})

        response = await self.client.send_prompt(command.prompt.content, context)

        return ResponseDTO(content=response)
