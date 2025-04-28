from typing import Sequence

from pydantic import Field

from src.application.common.dto import DTO
from src.application.chat.enums import MessageRole


class MessageDTO(DTO):
    id: int
    role: MessageRole
    content: str


class SendMessageDTO(DTO):
    role: MessageRole
    content: str


class ContextDTO(DTO):
    name: str
    content: str


class SendPromptDTO(DTO):
    content: str
    context: Sequence[ContextDTO] | None = Field(default=None)
    history: Sequence[SendMessageDTO] | None = Field(default=None)


class ResponseDTO(DTO):
    content: str
