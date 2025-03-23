from typing import Optional
from datetime import datetime

from app.pkg.models.base import BaseModel


__all__ = [
    "Post",
    "CreatePostCommand",
]


class BasePost(BaseModel):
    """Base model for posts"""


class Post(BasePost):
    channel_id: str
    message_id: int
    published_at: datetime
    text: Optional[str]
    views: Optional[int]
    collected_at: datetime


class CreatePostCommand(BasePost):
    channel_id: str
    message_id: int
    published_at: datetime
    text: Optional[str]
    views: Optional[int]
