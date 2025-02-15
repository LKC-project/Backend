from typing import Annotated

from fastapi import Depends
from didiator import Mediator

from src.presentation.api.providers.stub import Stub


MediatorDep = Annotated[Mediator, Depends(Stub(Mediator))]
