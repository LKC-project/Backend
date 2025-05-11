from fastapi import APIRouter, status

from src.application.google_drive.commands.upload_project import UploadProject
from src.application.google_drive.dto import UploadProjectResponseDTO

from src.presentation.api.providers.dependency import MediatorDep, CurrentUserIDDep
from src.presentation.api.exceptions import EXCEPTION_RESPONSE_MODEL


google_drive_router = APIRouter(prefix="/google-drive", tags=["Google Drive"])

routers = (google_drive_router, )


@google_drive_router.post(
    "/project",
    description="Збереження проєкту на гугл диск користувача",
    responses={
        status.HTTP_401_UNAUTHORIZED: EXCEPTION_RESPONSE_MODEL
    },
    status_code=status.HTTP_201_CREATED,
)
async def save_on_google_drive(
        mediator: MediatorDep,
        current_user_id: CurrentUserIDDep,
        data: UploadProject
) -> UploadProjectResponseDTO:
    return await mediator.send(data)
