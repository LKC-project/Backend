from typing import Annotated

from fastapi import Security

from src_.services.auth.auth import AuthService


auth_service = AuthService()


CurrentUserIDDep = Annotated[int, Security(auth_service.current_user_id)]
CurrentUserDep = Annotated[None, Security(lambda _: None)]
CurrentAdminIDDep = Annotated[None, Security(lambda _: None)]
CurrentAdminDep = Annotated[None, Security(lambda _: None)]
