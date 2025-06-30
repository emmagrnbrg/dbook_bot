import os

from aiogram import types
from functools import wraps

from dotenv import load_dotenv

from .constants import Messages, Settings

load_dotenv()


# данные канала и группы
CHANNEL_ID = os.getenv(Settings.CHANNEL_ID)
GROUP_ID = os.getenv(Settings.GROUP_ID)


def check_subscriptions():
    """
    Проверка подписок на каналы

    :return: основная функция (в случае, если пользователь подписан)
    """
    def decorator(handler_func):
        @wraps(handler_func)
        async def wrapper(message: types.Message, *args, **kwargs):
            user_id = message.from_user.id
            bot = message.bot

            async def is_subscribed(chat_id):
                """
                Проверка подписки на канал / группу

                :param chat_id: никнейм / id канала / группы
                :return: признак подписки
                """
                try:
                    member = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
                    return member.status not in ('left', 'kicked')
                except:
                    return False

            in_channel = await is_subscribed(CHANNEL_ID)
            in_group = await is_subscribed(GROUP_ID)

            if not (in_channel and in_group):
                await message.answer(Messages.GREETING.format(name=message.from_user.first_name,
                                                              channel=CHANNEL_ID,
                                                              group=GROUP_ID), parse_mode="MarkdownV2")
                return
            return await handler_func(message, *args, **kwargs)
        return wrapper
    return decorator
