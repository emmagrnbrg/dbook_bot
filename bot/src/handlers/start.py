from aiogram import types, Router
from aiogram.filters import CommandStart

from ..utils import check_subscriptions

router = Router()


@router.message(CommandStart())
@check_subscriptions()
async def start_handler(message: types.Message):
    await message.answer("Привет! Добро пожаловать в бота.")
