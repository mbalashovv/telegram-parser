from .posts import Posts
from .telegram import Telegram
from .telegram_posts import TelegramPosts

from app.internal.repository import Repository
from app.pkg.di import factory
from app.pkg.settings import settings
from app.pkg.logger import get_logger


class Services:
    logger = get_logger(__name__)

    posts_service = factory(
        Posts,
        post_repository=Repository.post_repository,
        logger=logger,
    )
    telegram_service = factory(
        Telegram,
        api_id=settings.TELEGRAM.API_ID,
        api_hash=settings.TELEGRAM.API_HASH,
        logger=logger,
    )
    telegram_posts_service = factory(
        TelegramPosts,
        posts_service=posts_service,
        telegram_service=telegram_service,
        logger=logger,
    )
