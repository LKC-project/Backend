from didiator import Mediator

from src.application.project.commands.upload_project import UploadProject, UploadProjectHandler
from src.application.project.commands.update_project import UpdateProject, UpdateProjectHandler
from src.application.project.queries.get_project import GetProjectByID, GetProjectByIDHandler
from src.application.project.queries.get_projects_by_user_id import GetProjectsByUserID, GetProjectsByUserIDHandler


def setup_project_handlers(mediator: Mediator):
    mediator.register_command_handler(UploadProject, UploadProjectHandler)
    mediator.register_command_handler(UpdateProject, UpdateProjectHandler)

    mediator.register_query_handler(GetProjectByID, GetProjectByIDHandler)
    mediator.register_query_handler(GetProjectsByUserID, GetProjectsByUserIDHandler)
