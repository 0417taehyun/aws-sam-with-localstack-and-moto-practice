from functools import lru_cache

from pydantic import BaseSettings     


class SlackSetting(BaseSettings):
    SLACK_BOT_TOKEN: str


class ApplicationSetting(SlackSetting):
    pass


@lru_cache
def get_setting() -> ApplicationSetting:
    return ApplicationSetting()
