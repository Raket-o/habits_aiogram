"""Модуль обработки просмотра привычек."""
from aiogram import types
from objects.user import user_obj
from utils.api_manager import ApiManager
from keyboards.inline.opers_habit import habit_opers_buttons


API_MANAGER = ApiManager()


async def get_detail_habit_hand_1(message: types.Message):
    """Функция get_detail_habit_hand_1. Отправляет запрос и выводит привычки пользователю."""
    await message.message.delete()
    data = message.data.split("=")
    habit_id = data[1]
    params = {"token": str(user_obj.token), "habit_id": int(habit_id)}

    status, response = await API_MANAGER.send_get(url="api/habits/<int:habit_id>", params=params)

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
