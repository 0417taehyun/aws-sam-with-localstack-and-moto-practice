from enum import Enum


class AWSServiceName(str, Enum):
    S3: str = "s3"


class AWSS3ClientMethod(str, Enum):
    GET_OBJECT: str = "get_object"
