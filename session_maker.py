import asyncio
import os
from telethon import TelegramClient

from app.pkg.settings import settings


async def main():
    # Create sessions folder with a session inside to fill it
    os.makedirs(os.path.dirname(settings.TELEGRAM.SESSION_PATH_EXTERNAL), exist_ok=True)
    with open(settings.TELEGRAM.SESSION_PATH_EXTERNAL, "w") as f:
        pass

    # You will need to enter login creds
    async with TelegramClient(
        settings.TELEGRAM.SESSION_PATH_EXTERNAL,
        settings.TELEGRAM.API_ID,
        settings.TELEGRAM.API_HASH,
    ) as client:
        pass

    # Now you can launch main program

asyncio.run(main())
