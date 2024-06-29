"""Модуль обработки просмотра записей."""
import aiohttp

from aiogram import types
# from aiogram.fsm.context import FSMContext

# from database import transactions
# from keyboards.reply.list_button import list_button
from objects.token import token_obj
from objects.user import user_obj
# from states.states import LoginUserState
# from utils.api_manager import ApiManager
from handlers.default_heandlers.start import start_command

# from handlers.custom_handlers.actioins_users.main_menu import main_menu_hand_1


# API_MANAGER = ApiManager()


async def logout_hand_1(message: types.Message):
    """Функция logout_hand_1. Запрашивает в базе записи и выводит их пользователю."""
    await message.message.delete()

    token_obj.__del__()
    user_obj.__del__()

    # print(user_obj)
    # print(token_obj)
    await start_command(message)
