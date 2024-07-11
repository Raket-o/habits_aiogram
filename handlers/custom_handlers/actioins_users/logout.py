"""Модуль логаут."""

from aiogram import types

from handlers.default_heandlers.start import start_command
from objects.token import token_obj
from objects.user import user_obj


async def logout_hand_1(message: types.Message):
    """Функция logout_hand_1. Очищает информацию о пользователе."""
    await message.message.delete()
    token_obj.__del__()
    user_obj.__del__()
    await start_command(message)
