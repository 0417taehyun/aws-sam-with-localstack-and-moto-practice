from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings


class AWSSetting(BaseSettings):
    AWS_REGION: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_ENDPOINT_URL: Optional[str]
    AWS_S3_BUCKET_NAME: str


class SlackSetting(BaseSettings):
    SLACK_CHANNEL_ID: str
    SLACK_BOT_TOKEN: str


class ApplicationSetting(AWSSetting, SlackSetting):
    pass


@lru_cache
def get_setting() -> ApplicationSetting:
    return ApplicationSetting()
