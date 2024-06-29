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
from keyboards.inline.opers_habit import habit_opers_buttons


API_MANAGER = ApiManager()


async def get_detail_habit_hand_1(message: types.Message, state: FSMContext):
    """Функция login_hand_1. Запрашивает в базе записи и выводит их пользователю."""
    await message.message.delete()

    data = message.data.split("=")
    habit_id = data[1]

    params = {"token": str(user_obj.token), "habit_id": int(habit_id)}
    # print("+="*20, params)

    status, response = await API_MANAGER.send_get(url="api/habits/<int:habit_id>", params=params)
    # print("+="*20, response)

    habit_id = response.get("id")
    habit_name = response.get("habit_name")
    description = response.get("description")
    alert_time = response.get("alert_time")
    count = response.get("count")

    txt = f"""Название привычки: {habit_name}
    Описание: {description}
    Время оповещения: {alert_time}
    Выполнено: {count}"""

    kb = habit_opers_buttons(habit_id)

    await message.message.answer(txt, reply_markup=kb)
