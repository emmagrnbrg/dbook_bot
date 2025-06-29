from enum import StrEnum


class Messages(StrEnum):
    """
    Тексты сообщений
    """
    GREETING = "*Привет,* {name}\! Для пользования ботом необходимо *подписаться* на наш *[канал](t.me/{channel})* " \
               " и *[группу](t.me/{group})* 🫶🏻"
