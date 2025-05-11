from didiator import Mediator

from src.application.google_drive.commands.upload_project import UploadProject, UploadProjectHandler


def setup_google_drive_handlers(mediator: Mediator):
    mediator.register_command_handler(UploadProject, UploadProjectHandler)
