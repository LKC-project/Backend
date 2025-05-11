from didiator import Mediator

from src.application.image.commands.upload_image import UploadImage, UploadImageHandler
from src.application.image.commands.upload_image_from_google_drive import (
    UploadImageFromGoogleDrive, UploadImageFromGoogleDriveHandler
)


def setup_image_handlers(mediator: Mediator):
    mediator.register_command_handler(UploadImage, UploadImageHandler)
    mediator.register_command_handler(UploadImageFromGoogleDrive, UploadImageFromGoogleDriveHandler)
