from typing import Annotated

from fastapi import APIRouter, UploadFile, File, status

from src.presentation.api.providers.dependency import MediatorDep, CurrentUserDep
from src.application.image.commands.upload_image import UploadImage
from src.application.image.dto import ImageDTO


image_router = APIRouter(prefix="/image", tags=["Images"])
images_router = APIRouter(prefix="/images", tags=["Images"])

routers = (image_router, images_router)


@image_router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    description="Завантаження зображення на CDN",
    dependencies=[CurrentUserDep]
)
async def post_image(
        mediator: MediatorDep,
        file: Annotated[UploadFile, File()]
) -> ImageDTO:
    img = await file.read()

    return await mediator.send(UploadImage(content=img))
