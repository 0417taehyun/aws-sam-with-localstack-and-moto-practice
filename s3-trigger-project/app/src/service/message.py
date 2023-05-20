from pydantic import HttpUrl

from src.custom import AWSLambdaEventBody
from src.service.s3 import AWSS3Service
from src.service.slack import SlackService


class MessageService:
    def __init__(self) -> None:
        self.s3: AWSS3Service = AWSS3Service()
        self.slack: SlackService = SlackService()

    def _parse_message(self, image_url: HttpUrl) -> str:
        return f"<!channel>\nYou can only see this <{image_url}|image> for 10 minutes!"

    def send_message_to_slack(self, event: AWSLambdaEventBody) -> None:
        object_key: str = event.get("Records").pop().get("s3").get("object").get("key")
        image_url: HttpUrl = self.s3.get_presigned_url(object_key=object_key)
        parsed_text: str = self._parse_message(image_url=image_url)
        self.slack.send_message(text=parsed_text)
