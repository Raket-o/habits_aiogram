"""Модуль обработки просмотра записей."""
import aiohttp

from aiogram import types
# from aiogram.fsm.context import FSMContext

# from database import transactions
# from keyboards.reply.list_button import list_button
# from objects.token import token_obj
from objects.user import user_obj
# from states.states import LoginUserState
from utils.api_manager import ApiManager
# from handlers.default_heandlers.start import start_command

from handlers.custom_handlers.actioins_users.main_menu import main_menu_hand_1
# from keyboards.inline.habit_opers import habit_opers_buttons


API_MANAGER = ApiManager()


# async def del_habit_hand_1(message: types.Message, state: FSMContext):
async def del_habit_hand_1(message: types.CallbackQuery):
    """Функция del_habit_hand_1. Запрашивает в базе записи и выводит их пользователю."""
    # await message.message.delete()

    data = message.data.split("=")
    habit_id = data[1]

    params = {"token": str(user_obj.token), "habit_id": int(habit_id)}
    # print("+="*20, params)

    status = await API_MANAGER.send_delete(url="api/habits/<int:habit_id>", params=params)

    await message.message.answer("Удалил" if status == 204 else "Не удача")

    await main_menu_hand_1(message)
