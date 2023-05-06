from functools import lru_cache

from pydantic import BaseSettings, HttpUrl


class DatabaseSetting(BaseSettings):
    DATABASE_HOST: str
    DATABASE_PORT: str = "3306"
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str = ""

    @property
    def DATABASE_URL(self) -> HttpUrl:
        USER_INFORMATION: str = ":".join([DatabaseSetting.DATABASE_USER, DatabaseSetting.DATABASE_PASSWORD])
        DATABASE_INFORMATION: str = ":".join([DatabaseSetting.DATABASE_HOST, DatabaseSetting.DATABASE_PORT])
        return f"mysql+mysqldb://{USER_INFORMATION}@{DATABASE_INFORMATION}/{DatabaseSetting.DATABASE_NAME}"


class SlackSetting(BaseSettings):
    SLACK_BOT_TOKEN: str


class ApplicationSetting(DatabaseSetting, SlackSetting):
    pass


@lru_cache
def get_setting() -> ApplicationSetting:
    return ApplicationSetting()
