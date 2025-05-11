from datetime import datetime

from aiohttp import ClientSession
from didiator import Command, CommandHandler

from src.application.google_drive.dto import UploadProjectDTO, UploadProjectResponseDTO


class UploadProject(UploadProjectDTO, Command[UploadProjectResponseDTO]):
    ...


class UploadProjectHandler(CommandHandler[UploadProject, UploadProjectResponseDTO]):
    async def __call__(self, command: UploadProject) -> UploadProjectResponseDTO:
        file = command.project.encode("utf-8")

        boundary = '*-_-+|+-_-*'
        metadata = {
            'name': f"Board-{datetime.now().strftime('%Y.%m.%d-%H:%M:%S')}.lkc",
            'mimeType': 'application/octet-stream'
        }

        multipart_body = (
             f'--{boundary}\r\n'
             'Content-Type: application/json; charset=UTF-8\r\n\r\n'
             f'{metadata}\r\n'
             f'--{boundary}\r\n'
             'Content-Type: application/octet-stream\r\n\r\n'
         ).encode('utf-8') + file + f'\r\n--{boundary}--'.encode('utf-8')

        headers = {
            'Authorization': f'Bearer {command.access_token}',
            'Content-Type': f'multipart/related; boundary={boundary}'
        }

        upload_url = 'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart'

        async with ClientSession() as session:
            async with session.post(upload_url, headers=headers, data=multipart_body) as resp:
                if resp.status != 200:
                    raise Exception(f"Upload failed: {resp.status} {await resp.text()}")

        return UploadProjectResponseDTO(
            file_name=metadata["name"]
        )
