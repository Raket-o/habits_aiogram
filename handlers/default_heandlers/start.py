""" Модуль команды /start."""
import logging

from aiogram import types

from config_data.config import START_MESSAGE
from keyboards.inline.greeting import greeting_buttons

start_logger = logging.getLogger(__name__)


async def start_command(message: [types.CallbackQuery, types.Message]) -> None:
    """
    Вывод тест START_MESSAGE и клавиатуру (регистрация, войти)
    """
    telegram_id = message.from_user.id
    full_name = message.from_user.full_name

    kb = greeting_buttons()

    if isinstance(message, types.Message):
        await message.answer(
            START_MESSAGE,
            parse_mode="HTML",
            reply_markup=kb
        )

    elif isinstance(message, types.CallbackQuery):
        await message.message.answer(
            START_MESSAGE,
            parse_mode="HTML",
            reply_markup=kb
        )

    start_logger.info(f"start_logger-UserID={telegram_id} {full_name}")
