from aiohttp import ClientSession

from didiator import Command, CommandHandler

from src.application.image.dto import UploadImageFromGoogleDriveDTO, ImageDTO
from src.infrastructure.s3 import ObjectStorage


class UploadImageFromGoogleDrive(UploadImageFromGoogleDriveDTO, Command[ImageDTO]):
    pass


class UploadImageFromGoogleDriveHandler(CommandHandler[UploadImageFromGoogleDrive, ImageDTO]):
    def __init__(self, object_storage: ObjectStorage):
        self.object_storage = object_storage

    async def __call__(self, command: UploadImageFromGoogleDrive) -> ImageDTO:
        url = f"https://www.googleapis.com/drive/v3/files/{command.file_id}?alt=media"
        headers = {"Authorization": f"Bearer {command.access_token}"}

        async with ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    image = await response.read()
                else:
                    raise Exception(f"Ошибка {response}")

        url = await self.object_storage.put_object(image)

        return ImageDTO(url=url)

