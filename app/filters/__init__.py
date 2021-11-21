from aiogram import Dispatcher
from loguru import logger

from .is_reply import IsReplyFilter


async def setup(dispatcher: Dispatcher):

    text_messages = [
        dispatcher.message_handlers,
        dispatcher.edited_message_handlers,
        dispatcher.channel_post_handlers,
        dispatcher.edited_channel_post_handlers,
    ]

    dispatcher.filters_factory.bind(IsReplyFilter, event_handlers=text_messages)

    logger.info('Filters are successfully configured')
