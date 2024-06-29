""" Модуль инициализации телеграмм бота."""
import logging
from asyncio import get_event_loop

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config_data.config import BOT_TOKEN

logger = logging.getLogger(__name__)


async def start_up():
    """Функция start_up. При запуске выводит текст в консоль."""
    logging.info("Bot started")


async def on_shutdown():
    """Функция on_shutdown. При завершении выводит текст в консоль."""
    logging.info("Bot stopped")

# from aiogram.client.session.aiohttp import AiohttpSession
# from aiogram.client.telegram import TelegramAPIServer
# session = AiohttpSession(
#     # api=TelegramAPIServer.from_base('http://0.0.0.0:8000')
#     api=TelegramAPIServer.from_base('https://api.telegram.org/')
# )
# # session = AiohttpSession(proxy="https://api.telegram.org/")
#
# bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML, session=session)
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
loop = get_event_loop()
dp = Dispatcher()
