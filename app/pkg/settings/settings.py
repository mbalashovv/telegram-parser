import urllib.parse
from functools import lru_cache
from typing import Optional, List, Literal
from pathlib import Path

from dotenv import find_dotenv
from pydantic import PostgresDsn, model_validator
from pydantic.types import PositiveInt, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

__all__ = ["get_settings"]


class _Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        arbitrary_types_allowed=True,
        case_sensitive=True,
        env_nested_delimiter="__",
        extra="allow",
    )


class Postgresql(_Settings):
    """Postgresql settings."""

    #: str: Postgresql host.
    HOST: str = "localhost"
    #: PositiveInt: positive int (x > 0) port of postgresql.
    PORT: PositiveInt = 5432
    #: str: Postgresql user.
    USER: str = "postgres"
    #: SecretStr: Postgresql password.
    PASSWORD: SecretStr = SecretStr("postgres")
    #: str: Postgresql database name.
    DATABASE_NAME: str = "postgres"

    #: str: Concatenation all settings for postgresql in one string. (DSN)
    DSN: Optional[str] = None

    @model_validator(mode="after")
    @classmethod
    def build_dsn(cls, values: "Postgresql"):  # pylint: disable=no-self-argument
        """Build DSN for postgresql."""

        values.DSN = str(
            PostgresDsn.build(
                scheme="postgresql",
                username=values.USER,
                password=urllib.parse.quote_plus(values.PASSWORD.get_secret_value()),
                host=values.HOST,
                port=int(values.PORT),
                path=values.DATABASE_NAME,
            ),
        )

        return values


class Telegram(_Settings):
    """Postgresql settings."""
    #: int: Telegram api id. You can get it on https://my.telegram.org/
    API_ID: int
    #: str: Telegram api hash. You can get it on https://my.telegram.org/
    API_HASH: str
    #: List[int]: Telegram sources (channels/groups) to parse.
    SOURCES_TO_PARSE: List[int]
    #: str: Path of a telegram session.
    SESSION_PATH: Path
    #: str: Path of a telegram session on your local machine.
    SESSION_PATH_EXTERNAL: Path


class Logger(_Settings):
    LEVEL: Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"]
    FILE_PATH: Path


class Settings(_Settings):
    """Server settings.

    Formed from `.env`.
    """

    #: int: Number of messages to be parsed.
    MESSAGES_NUMBER: int = 50
    #: int: Sleeping time in minutes for every iteration.
    SLEEP_TIME_MINUTES: int = 60
    #: Postgresql: Postgresql settings.
    POSTGRES: Postgresql
    #: Telegram: Telegram settings.
    TELEGRAM: Telegram
    #: Logger: Logger settings.
    LOGGER: Logger


@lru_cache
def get_settings(env_file: str = ".env") -> Settings:
    """Create settings instance."""
    return Settings(_env_file=find_dotenv(env_file))
