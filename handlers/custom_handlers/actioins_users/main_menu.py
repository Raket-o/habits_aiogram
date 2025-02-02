"""Модуль главного меню."""

from aiogram import types

from keyboards.inline.main_menu import main_menu_buttons
from objects.user import user_obj
from utils.api_manager import ApiManager

API_MANAGER = ApiManager()


async def main_menu_hand_1(message: [types.CallbackQuery, types.Message]):
    """
    Функция main_menu_hand_1.
    Отправляет запрос и выводит список привычек пользователю.
    """
    params = {"token": str(user_obj.token)}
    status, response_json = await API_MANAGER.send_get(
        url="api/users/me/", params=params
    )
    habits = response_json.get("habits")

    if habits:
        tpl_habits = tuple(
            (habit.get("id"), habit.get("habit_name")) for habit in habits
        )
    else:
        tpl_habits = None
    kb = main_menu_buttons(tpl_habits)
    txt = "Привычки:" if habits else "Пока нет привычек"

    if isinstance(message, types.Message):
        await message.answer(txt, reply_markup=kb)

    elif isinstance(message, types.CallbackQuery):
        await message.message.answer(txt, reply_markup=kb)
        await message.message.delete()
