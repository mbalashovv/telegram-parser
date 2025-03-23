import logging
from typing import List, Union, Tuple
from telethon import TelegramClient
from telethon.tl.types import Message, Chat, Channel

from app.pkg.settings import settings

__all__ = ["Telegram"]


class Telegram:
    """Service for manage telegram."""

    __api_id: int
    __api_hash: str

    def __init__(
        self,
        api_id: int,
        api_hash: str,
        logger: logging.Logger,
    ):
        self.__api_id = api_id
        self.__api_hash = api_hash
        self.logger = logger

    async def get_source_messages(
        self,
        source_id: int,
    ) -> Tuple[Union[Channel, Chat], List[Message]]:
        async with TelegramClient(settings.TELEGRAM.SESSION_PATH, self.__api_id, self.__api_hash) as client:
            entity = await client.get_entity(source_id)  # Get the chat/channel entity
            messages = await client.get_messages(entity, limit=settings.MESSAGES_NUMBER)
        return entity, messages
