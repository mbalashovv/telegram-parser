import logging
from typing import Tuple

from app.internal.services.posts import Posts
from app.internal.services.telegram import Telegram
from app.pkg.models.exceptions import PostAlreadyExists
from app.pkg import models

__all__ = ["TelegramPosts"]


class TelegramPosts:
    """Service for manage both telegram and posts."""

    __telegram_service: Telegram
    __posts_service: Posts

    def __init__(
        self,
        telegram_service: Telegram,
        posts_service: Posts,
        logger: logging.Logger
    ):
        self.__telegram_service = telegram_service
        self.__posts_service = posts_service
        self.logger = logger

    async def parse_source(
        self,
        source_id: int,
    ) -> Tuple[str, int, int]:
        entity, messages = await self.__telegram_service.get_source_messages(source_id=source_id)
        errors_count = 0
        for message in messages:
            try:
                await self.__posts_service.create(
                    cmd=models.CreatePostCommand(
                        channel_id=str(source_id),
                        message_id=message.id,
                        published_at=message.date.replace(tzinfo=None),
                        text=message.message,
                        views=message.views,
                    )
                )
            except PostAlreadyExists:
                errors_count += 1
                pass
        return entity.title, len(messages), len(messages) - errors_count
