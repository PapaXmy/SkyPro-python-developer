class BaseServiceError(Exception):
    code = 500


class ItemNotFound(BaseServiceError):
    code = 404


class Unauthorized(BaseServiceError):
    code = 401


class DuplicateMovie(BaseServiceError):
    pass
