import asyncio
import time

from app.internal import services
from app.pkg.di import inject

from app.pkg.logger import get_logger
from app.pkg.settings import settings


logger = get_logger(__name__)


async def main(
    telegram_posts: services.TelegramPosts = inject(services.Services.telegram_posts_service)
) -> None:
    while True:
        all_statistics = []
        for source_id in settings.TELEGRAM.SOURCES_TO_PARSE:
            all_statistics.append(await telegram_posts.parse_source(source_id=source_id))

        for channel_statistics in all_statistics:
            logger.info(f"Parsed \"%s\": got %s messages, created: %s", *channel_statistics)

        logger.info("The iteration ended. Gonna sleep for %s minutes", settings.SLEEP_TIME_MINUTES)

        await asyncio.sleep(settings.SLEEP_TIME_MINUTES * 60)


if __name__ == "__main__":
    try:
        while True:
            asyncio.run(main())
    except Exception as exc:
        logger.exception("Got an exception %s", exc)
        time.sleep(settings.SLEEP_TIME_MINUTES * 60)
