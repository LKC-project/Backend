from didiator import Mediator

from src.application.image.commands.upload_image import UploadImage, UploadImageHandler


def setup_image_handlers(mediator: Mediator):
    mediator.register_command_handler(UploadImage, UploadImageHandler)
