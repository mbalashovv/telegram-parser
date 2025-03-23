from app.internal.repository.connection import get_connection
from app.internal.repository.handlers.collect_response import (
    collect_response,
)
from app.internal.repository.base import BaseRepository
from app.pkg import models

__all__ = ["PostRepository"]


class PostRepository(BaseRepository):
    """Post repository implementation."""

    @collect_response
    async def create(self, cmd: models.CreatePostCommand) -> models.Post:
        q = """
            INSERT INTO telegram_posts(channel_id, message_id, published_at, text, views)
            SELECT $1, $2, $3, $4, $5
            WHERE NOT EXISTS (
                SELECT 1 FROM telegram_posts 
                WHERE channel_id = $1 AND message_id = $2
            )
            RETURNING *;
        """
        values = list(cmd.model_dump().values())
        async with get_connection() as cur:
            return await cur.fetchrow(q, *values)

