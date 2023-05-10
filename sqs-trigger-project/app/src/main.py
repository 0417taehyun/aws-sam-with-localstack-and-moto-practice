import json
from logging import DEBUG, Logger, getLogger

from src.constant import HTTPStatusCode
from src.custom import AWSLambdaContext, AWSLambdaEventBody, HTTPResponse
from src.service import MessageService


def lambda_handler(event: AWSLambdaEventBody, context: AWSLambdaContext):
    logger: Logger = getLogger()
    logger.setLevel(level=DEBUG)
    message: MessageService = MessageService()
    try:
        message.send_message_to_slack(event=event)
        return HTTPResponse(
            statusCode=HTTPStatusCode.OK.value,
            headers={"Content-Type": "application/json"},
            body=json.dumps(obj={"detail": "Success"}),
        )

    except ValueError as value_error:
        return HTTPResponse(
            statusCode=HTTPStatusCode.BAD_REQUEST.value,
            headers={"Content-Type": "application/json"},
            body=json.dumps(obj={"detail": str(value_error)}),
        )

    except Exception as unhandled_error:
        return HTTPResponse(
            statusCode=HTTPStatusCode.INTERNAL_SERVER_ERROR.value,
            headers={"Content-Type": "application/json"},
            body=json.dumps(obj={"detail": str(unhandled_error)}),
        )
