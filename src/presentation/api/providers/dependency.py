from typing import Annotated

from fastapi import Depends, Security
from didiator import Mediator

from src.presentation.api.providers.stub import Stub
from src.presentation.api.providers.auth import auth_provider


MediatorDep = Annotated[Mediator, Depends(Stub(Mediator))]

CurrentUserIDDep = Annotated[int, Security(auth_provider.current_user_id)]
CurrentUserIDOrNoneDep = Annotated[int, Security(auth_provider.current_user_id)]
