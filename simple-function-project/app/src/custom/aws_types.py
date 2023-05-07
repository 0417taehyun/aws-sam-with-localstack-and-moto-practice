from dataclasses import dataclass
from typing import Optional, TypedDict


class AWSLambdaEventBody(TypedDict):
    channel: str
    nickname: str
    message: str


@dataclass
class AWSLambdaContext:
    aws_request_id: str
    log_group_name: str
    log_stream_name: str
    function_name: str
    memory_limit_in_mb: int
    function_version: str
    invoked_function_arn: str
    identity: Optional[dict] = None
    client_context: Optional[dict] = None
