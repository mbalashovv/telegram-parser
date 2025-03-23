from app.pkg.di import factory
from .posts import PostRepository

__all__ = ["Repository"]


class Repository:
    post_repository = factory(PostRepository)
