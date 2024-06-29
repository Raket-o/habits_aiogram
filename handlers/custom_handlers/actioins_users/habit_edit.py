"""Модуль обработки просмотра записей."""
import aiohttp
import datetime

from aiogram import types
from aiogram.fsm.context import FSMContext

# from database import transactions
# from keyboards.reply.list_button import list_button
# from objects.token import token_obj
from objects.user import user_obj
from states.states import EditHabitState
from utils.api_manager import ApiManager
# from handlers.default_heandlers.start import start_command

from handlers.custom_handlers.actioins_users.main_menu import main_menu_hand_1
# from keyboards.inline.habit_opers import habit_opers_buttons
from keyboards.inline.habit_edit_btns import edit_habit_buttons


API_MANAGER = ApiManager()


# async def del_habit_hand_1(message: types.Message, state: FSMContext):
async def edit_habit_hand(message: [types.CallbackQuery, types.Message]):
    """Функция edit_name_habit_hand_1. Запрашивает в базе записи и выводит их пользователю."""
    await message.message.delete()
    data = message.data.split("=")
    habit_id = int(data[1])
    print("edit_habit_hand="*5, habit_id)

    kb = edit_habit_buttons(habit_id)

    await message.message.answer("Что будем изменять", reply_markup=kb)


async def edit_name_habit_hand_1(message: types.CallbackQuery, state: FSMContext
) -> None:
    """Функция edit_name_habit_hand_1. Запрашивает в базе записи и выводит их пользователю."""
    await message.message.delete()
    data = message.data.split("=")
    habit_id = data[1]
    await state.update_data({"habit_id": habit_id})

    await message.message.answer("Введите новое название")

    await state.set_state(EditHabitState.name)


async def edit_name_habit_hand_2(message: types.CallbackQuery, state: FSMContext) -> None:
    """Функция edit_name_habit_hand_1. Запрашивает в базе записи и выводит их пользователю."""
    await message.delete()

    habit_name = message.text

    context_data = await state.get_data()
    habit_id = context_data.get("habit_id")
    params = {"token": str(user_obj.token), "habit_id": int(habit_id)}
    data = {"habit_name": habit_name}

    status = await API_MANAGER.send_patch(url="api/habits/<int:habit_id>", json=data, params=params)

    await message.answer("Изменил" if status == 201 else "Не удача")
    await state.clear()
    await main_menu_hand_1(message)


async def edit_description_habit_hand_1(message: types.CallbackQuery, state: FSMContext
) -> None:
    """Функция edit_name_habit_hand_1. Запрашивает в базе записи и выводит их пользователю."""
    await message.message.delete()
    data = message.data.split("=")
    habit_id = data[1]
    await state.update_data({"habit_id": habit_id})

    await message.message.answer("Введите новое описание")

    await state.set_state(EditHabitState.description)


async def edit_description_habit_hand_2(message: types.CallbackQuery, state: FSMContext) -> None:
    """Функция edit_name_habit_hand_1. Запрашивает в базе записи и выводит их пользователю."""
    await message.delete()

    description = message.text

    context_data = await state.get_data()
    habit_id = context_data.get("habit_id")
    params = {"token": str(user_obj.token), "habit_id": int(habit_id)}
    data = {"description": description}

    status = await API_MANAGER.send_patch(url="api/habits/<int:habit_id>", json=data, params=params)

    await message.answer("Изменил" if status == 201 else "Не удача")
    await state.clear()
    await main_menu_hand_1(message)


async def edit_alert_time_habit_hand_1(message: types.CallbackQuery, state: FSMContext
                                        ) -> None:
    """Функция edit_name_habit_hand_1. Запрашивает в базе записи и выводит их пользователю."""
    await message.message.delete()
    data = message.data.split("=")
    habit_id = data[1]
    await state.update_data({"habit_id": habit_id})

    await message.message.answer("Введите новое время")

    await state.set_state(EditHabitState.alert_time)


async def edit_alert_time_habit_hand_2(message: types.CallbackQuery, state: FSMContext) -> None:
    """Функция edit_alert_time_habit_hand_2. Запрашивает в базе записи и выводит их пользователю."""
    await message.delete()

    alert_time = message.text

    try:
        alert_time = datetime.datetime.strptime(alert_time, '%H-%M').time()

        context_data = await state.get_data()
        habit_id = context_data.get("habit_id")
        params = {"token": str(user_obj.token), "habit_id": int(habit_id)}
        data = {"alert_time": str(alert_time)}

        status = await API_MANAGER.send_patch(url="api/habits/<int:habit_id>", json=data, params=params)

        await message.answer("Изменил" if status == 201 else "Не удача")
        await state.clear()
        await main_menu_hand_1(message)
    except ValueError:
        await message.answer("Напишите время в формате ЧЧ-ММ. Пример 16-55")
