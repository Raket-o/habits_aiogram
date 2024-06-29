"""Модуль обработки просмотра записей."""
import aiohttp

from aiogram import types
from aiogram.fsm.context import FSMContext

# from database import transactions
# from keyboards.reply.list_button import list_button
from objects.token import token_obj
from objects.user import user_obj
from states.states import LoginUserState
from utils.api_manager import ApiManager
from handlers.default_heandlers.start import start_command

from handlers.custom_handlers.actioins_users.main_menu import main_menu_hand_1


API_MANAGER = ApiManager()


async def login_hand_1(message: types.Message, state: FSMContext):
    """Функция login_hand_1. Запрашивает в базе записи и выводит их пользователю."""
    await message.message.delete()
    await message.message.answer("Введите имя")
    await state.set_state(LoginUserState.username)


async def login_hand_2(message: types.Message, state: FSMContext):
    """Функция login_hand_2. Запрашивает в базе записи и выводит их пользователю."""
    await message.delete()
    username = message.text
    await state.update_data({"username": username})

    await message.answer("Введите пароль")
    await state.set_state(LoginUserState.password)


async def login_hand_3(message: types.Message, state: FSMContext):
    """Функция login_hand_3. Запрашивает в базе записи и выводит их пользователю."""
    await message.delete()
    context_data = await state.get_data()
    username = context_data.get("username")
    password = message.text
    telegram_id = message.from_user.id

    data = {"username": username, "password": password}

    status, response = await API_MANAGER.send_post(url="api/auth/token", data=data)

    if status != 200:
        await message.answer("неверное имя или пароль")
        await start_command(message)
    else:
        token_obj.token = response.get("access_token")
        user_obj.telegram_id = telegram_id
        user_obj.username = username
        user_obj.token = token_obj
        # print(user_obj)
        await state.clear()

        await main_menu_hand_1(message)
