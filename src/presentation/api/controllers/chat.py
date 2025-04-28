from typing import Annotated

from fastapi import APIRouter, Path, status

from src.application.chat.dto import SendPromptDTO, ResponseDTO
from src.application.chat.commands.send_prompt import SendPrompt

from src.presentation.api.providers.dependency import MediatorDep, CurrentUserIDDep, CurrentUserDep
from src.presentation.api.exceptions import EXCEPTION_RESPONSE_MODEL


chat_router = APIRouter(prefix="/chat", tags=["Chat"])

routers = (chat_router, )


@chat_router.post(
    "/{project_id}/message",
    description="Відправляє запит для обробки ШІ"
)
async def post_message(
        mediator: MediatorDep,
        current_user_id: CurrentUserIDDep,
        project_id: Annotated[int, Path()],
        prompt: SendPromptDTO
) -> ResponseDTO:
    return await mediator.send(SendPrompt(project_id=project_id, prompt=prompt))
