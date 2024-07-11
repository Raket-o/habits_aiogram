"""Модуль удаления привычки."""

from aiogram import types

from handlers.custom_handlers.actioins_users.main_menu import main_menu_hand_1
from objects.user import user_obj
from utils.api_manager import ApiManager

API_MANAGER = ApiManager()


async def del_habit_hand_1(message: types.CallbackQuery):
    """Функция del_habit_hand_1. Отправляет запрос на удаление привычки."""
    data = message.data.split("=")
    habit_id = data[1]
    params = {"token": str(user_obj.token), "habit_id": int(habit_id)}
    status = await API_MANAGER.send_delete(
        url="api/habits/<int:habit_id>", params=params
    )
    await message.message.answer("Удалил" if status == 204 else "Не удача")
    await main_menu_hand_1(message)
