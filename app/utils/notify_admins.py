from asyncio import sleep

from loguru import logger

from app.config import ADMINS_ID
from app.utils.broadcaster import send_message


async def notify_admins():
    count = 0
    try:
        for admin_id in ADMINS_ID:
            if await send_message(admin_id, 'The bot is running!'):
                count += 1
            await sleep(.05)  # 20 messages per second (Limit: 30 messages per second)
    finally:
        logger.info(f"{count} messages successful sent.")
