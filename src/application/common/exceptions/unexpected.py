from src.application.common.exceptions.base import UnexpectedError


class CommitError(UnexpectedError):
    pass


class RollbackError(UnexpectedError):
    pass
