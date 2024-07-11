"""Модуль обработки создание привычки."""
import datetime

from aiogram import types
from aiogram.fsm.context import FSMContext

from states.states import CreateHabitState
from utils.api_manager import ApiManager
from handlers.custom_handlers.actioins_users.main_menu import main_menu_hand_1

from objects.user import user_obj


API_MANAGER = ApiManager()


async def create_habit_hand_1(message: types.Message, state: FSMContext) -> None:
    """Функция create_habit_hand_1. Ожидает ввод от пользователя."""
    await message.message.delete()
    await message.message.answer("Введите название привычки")
    await state.set_state(CreateHabitState.name)


async def create_habit_hand_2(message: types.Message, state: FSMContext) -> None:
    """Функция create_habit_hand_2. Ожидает ввод от пользователя."""
    await message.delete()
    habit_name = message.text
    await state.update_data({"habit_name": habit_name})
    await message.answer("Введите описание")
    await state.set_state(CreateHabitState.description)


async def create_habit_hand_3(message: types.Message, state: FSMContext) -> None:
    """Функция create_habit_hand_3. Ожидает ввод от пользователя."""
    await message.delete()
    habit_description = message.text
    await state.update_data({"habit_description": habit_description})
    await message.answer("Введите время оповещения в формате ЧЧ-ММ")
    await state.set_state(CreateHabitState.alert_time)


async def create_habit_hand_4(message: types.Message, state: FSMContext) -> None:
    """Функция create_habit_hand_4. Отправляет запрос на создание привычки."""

    await message.delete()
    alert_time = message.text

    try:
        alert_time = datetime.datetime.strptime(alert_time, '%H-%M').time()

        context_data = await state.get_data()
        params = {"token": str(user_obj.token)}
        habit_name = context_data.get("habit_name")
        description = context_data.get("habit_description")

        data = {"habit_name": habit_name, "description": description, "alert_time": str(alert_time)}

        status, response = await API_MANAGER.send_post(url="api/habits/", json=data, params=params)

        if status == 201:
            txt = "Привычка добавлена"
        else:
            txt = "Что-то пошло не так. Попробуйте ещё раз"

        await message.answer(txt)
        await main_menu_hand_1(message)
        await state.clear()

    except ValueError:
        await message.answer("Напишите время в формате ЧЧ-ММ. Пример 16-55")


