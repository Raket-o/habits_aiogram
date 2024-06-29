"""Модуль обработки просмотра записей."""
import aiohttp

from aiogram import types
from aiogram.fsm.context import FSMContext

from objects.user import user_obj
from keyboards.inline.main_menu import main_menu_buttons
from utils.api_manager import ApiManager


API_MANAGER = ApiManager()


async def main_menu_hand_1(message: [types.CallbackQuery, types.Message]):
    """Функция main_menu_hand_1. Запрашивает в базе записи и выводит их пользователю."""
    params = {"token": str(user_obj.token)}
    status, response_json = await API_MANAGER.send_get(url="api/users/me/", params=params)
    habits = response_json.get("habits")

    if habits:
        tpl_habits = tuple((habit.get("id"), habit.get("habit_name")) for habit in habits)
    else:
        tpl_habits = None
    kb = main_menu_buttons(tpl_habits)
    txt = "Привычки:" if habits else "Пока нет привычек"

    if isinstance(message, types.Message):
        await message.answer(txt, reply_markup=kb)
        # await message.delete()

    elif isinstance(message, types.CallbackQuery):
        await message.message.answer(txt, reply_markup=kb)
        await message.message.delete()
