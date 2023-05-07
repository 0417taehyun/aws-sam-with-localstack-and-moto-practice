from enum import Enum


class HTTPStatusCode(Enum):
    OK: int = 200
    BAD_REQUEST: int = 400
    INTERNAL_SERVER_ERROR: int = 500
