from didiator import Command, CommandHandler

from src.application.image.dto import UploadImageDTO, ImageDTO
from src.infrastructure.s3 import ObjectStorage


class UploadImage(UploadImageDTO, Command[ImageDTO]):
    pass


class UploadImageHandler(CommandHandler[UploadImage, ImageDTO]):
    def __init__(self, object_storage: ObjectStorage):
        self.object_storage = object_storage

    async def __call__(self, command: UploadImage) -> ImageDTO:
        url = await self.object_storage.put_object(command.content)

        return ImageDTO(
            url=url
        )

