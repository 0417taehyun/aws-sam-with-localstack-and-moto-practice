from src.custom import AWSLambdaEventBody
from src.service.slack import SlackService


class MessageService:
    def __init__(self) -> None:
        self.slack: SlackService = SlackService()

    def _parse_message(self, event: AWSLambdaEventBody) -> str:
        nickname: str = event.get("nickname")
        message: str = event.get("message")
        return f"<!channel>\nThe below message was sent from {nickname}.\n\n```{message}```"

    def send_message_to_slack(self, event: AWSLambdaEventBody) -> None:
        channel: str = event.get("channel")
        parsed_text: str = self._parse_message(event=event)
        self.slack.send_message(channel=channel, text=parsed_text)
