""" Модуль запуска телеграмм бота."""
import asyncio

from aiogram import Bot, Dispatcher

from handlers.routers import register_routers
from loader import bot, dp, on_shutdown, start_up
from utils import logging


async def main(bot: Bot, dp: Dispatcher) -> None:
    """Функция main. Запускает бота."""
    dp.startup.register(start_up)
    dp.shutdown.register(on_shutdown)

    register_routers(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main(bot, dp))
    # URL_BACKEND_SERVER = "http://192.168.55.5:8000"
