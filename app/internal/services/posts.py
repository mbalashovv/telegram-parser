import logging

from app.internal.repository.posts import PostRepository
from app.pkg.models.exceptions import EmptyResult, PostAlreadyExists
from app.pkg import models

__all__ = ["Posts"]


class Posts:
    """Service for manage posts."""

    __post_repository: PostRepository

    def __init__(
        self,
        post_repository: PostRepository,
        logger: logging.Logger,
    ):
        self.__post_repository = post_repository
        self.logger = logger

    async def create(self, cmd: models.CreatePostCommand) -> models.Post:
        try:
            post = await self.__post_repository.create(cmd=cmd)
        except EmptyResult as e:
            self.logger.exception("Post already exists, couldn't create: %s", cmd)
            raise PostAlreadyExists from e

        self.logger.info("Created a post: %s", post)
        return post
