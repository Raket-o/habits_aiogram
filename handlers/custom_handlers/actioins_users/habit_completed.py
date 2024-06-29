"""Модуль обработки просмотра записей."""
import datetime

from aiogram import types
from aiogram.fsm.context import FSMContext

from states.states import CreateHabitState
from utils.api_manager import ApiManager
from handlers.custom_handlers.actioins_users.main_menu import main_menu_hand_1

from objects.user import user_obj


API_MANAGER = ApiManager()


async def habit_comp_1(message: types.Message) -> None:
    """Функция habit_comp_1. Запрашивает в базе записи и выводит их пользователю."""
    # await message.message.delete()
    data = message.data.split("=")
    habit_id = data[1]
    params = {"token": str(user_obj.token), "habit_id": int(habit_id)}

    status, response = await API_MANAGER.send_post(url="api/habits/<int:habit_id>/fulfilling", params=params)

    if status == 201:
        txt = "Вы молодец, я в это верил"
        await message.message.delete()
    elif status == 401:
        txt = "Не получилось зафиксировать результат. Выйдите под собой"
    else:
        txt = "Что-то пошло не так. Попробуйте ещё раз"
        await message.message.delete()

    await message.answer(txt)
    # await message.message.delete()


async def habit_did_not_comp_1(message: types.Message) -> None:
    """Функция habit_did_not_comp_1. Запрашивает в базе записи и выводит их пользователю."""
    await message.answer("Это печально")
    await message.message.delete()
