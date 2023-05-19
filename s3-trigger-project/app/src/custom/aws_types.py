from dataclasses import dataclass
from typing import Optional, TypedDict


class AWSSQSMessage(TypedDict):
    channel: str
    nickname: str
    message: str


class AWSSQSAttribute(TypedDict):
    ApproximateReceiveCount: str
    SentTimestamp: str
    SenderId: str
    ApproximateFirstReceiveTimestamp: str


class AWSSQSRecord(TypedDict):
    messageId: str
    receiptHandle: str
    body: str
    attributes: AWSSQSAttribute
    messageAttributes: Optional[dict]
    md5OfBody: str
    eventSource: str
    eventSourceARN: str
    awsRegion: str


class AWSLambdaEventBody(TypedDict):
    Records: list[AWSSQSRecord]


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
