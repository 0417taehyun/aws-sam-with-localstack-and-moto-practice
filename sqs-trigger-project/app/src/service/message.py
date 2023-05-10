import json

from src.custom import AWSLambdaEventBody, AWSSQSMessage
from src.service.slack import SlackService


class MessageService:
    def __init__(self) -> None:
        self.slack: SlackService = SlackService()

    def _parse_message(self, body: AWSSQSMessage) -> str:
        message: str = body.get("message")
        nickname: str = body.get("nickname")
        return f"<!channel>\nThe below message was sent from {nickname}.\n\n```{message}```"

    def send_message_to_slack(self, event: AWSLambdaEventBody) -> None:
        body: AWSSQSMessage = json.loads(s=event.get("Records").pop().get("body"))
        channel: str = body.get("channel")
        parsed_text: str = self._parse_message(body=body)
        self.slack.send_message(channel=channel, text=parsed_text)
