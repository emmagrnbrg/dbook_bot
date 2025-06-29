import logging
import os
from enum import StrEnum


class Settings(StrEnum):
    """
    Настройки проекта
    """
    # настройки Telegram-бота
    BOT_TOKEN = "BOT_TOKEN"

    # данные канала
    CHANNEL_ID = "CHANNEL_ID"
    GROUP_ID = "GROUP_ID"

    # Ю-Касса
    YOOKASSA_TOKEN = "YOOKASSA_TOKEN"

    # БД (Postgres)
    POSTGRES_USER = "POSTGRES_USER"
    POSTGRES_PASSWORD = "POSTGRES_PASSWORD"
    POSTGRES_DB = "POSTGRES_DB"
    POSTGRES_HOST = "POSTGRES_HOST"


def get_logger(name: str) -> logging.Logger:
    """
    Конфигурация логирования

    :param name: наименование логгера
    :return: логгер
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    log_format = "%(asctime)s [%(levelname)s] %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S.%f"

    formatter = logging.Formatter(fmt=log_format, datefmt=date_format)

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        file_path = os.path.join(log_dir, f"{name}.log")
        file_handler = logging.FileHandler(file_path, mode="a", encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
