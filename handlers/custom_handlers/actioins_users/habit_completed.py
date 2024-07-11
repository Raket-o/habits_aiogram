"""Модуль обработки ответа от пользователя выполнил ли привычку или нет."""
from aiogram import types
from utils.api_manager import ApiManager
from objects.user import user_obj


API_MANAGER = ApiManager()


async def habit_comp_1(message: types.Message) -> None:
    """Функция habit_comp_1. Проставляет выполнение привычки."""
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


async def habit_did_not_comp_1(message: types.Message) -> None:
    """Функция habit_did_not_comp_1. Выводи сообщение и удаляет предыдущие."""
    await message.answer("Это печально")
    await message.message.delete()
