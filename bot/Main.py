import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from src.handlers import setup_routers
from src.config.config import Settings


load_dotenv()

# токен
TELEGRAM_TOKEN = os.getenv(Settings.BOT_TOKEN)

# бот
BOT = Bot(token=TELEGRAM_TOKEN)
DP = Dispatcher(storage=MemoryStorage())

setup_routers(DP)


async def main():
    await DP.start_polling(BOT)

if __name__ == "__main__":
    asyncio.run(main())
