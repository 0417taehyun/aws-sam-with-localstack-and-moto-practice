from slack_sdk import WebClient
from slack_sdk.web import SlackResponse

from src.core import get_setting


class SlackService:
    _SLACK_CHANNEL_ID: str = get_setting().SLACK_CHANNEL_ID

    def __init__(self) -> None:
        self.client: WebClient = WebClient(token=get_setting().SLACK_BOT_TOKEN)

    def send_message(self, text: str) -> None:
        response: SlackResponse = self.client.chat_postMessage(channel=SlackService._SLACK_CHANNEL_ID, text=text)
        if not response.get("ok"):
            raise ValueError(response.get("error"))
