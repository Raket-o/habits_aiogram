"""Модуль регистрации пользователя."""
from aiogram import types
from aiogram.fsm.context import FSMContext
from states.states import RegisterUserState
from utils.api_manager import ApiManager
from handlers.default_heandlers.start import start_command
from keyboards.inline.cancel import cancel_buttons


API_MANAGER = ApiManager()
KB = cancel_buttons()


async def register_hand_1(message: types.Message, state: FSMContext):
    """Функция register_hand_1. Ожидает ввод от пользователя.."""
    await message.message.delete()
    await message.message.answer("Введите имя", reply_markup=KB)
    await state.set_state(RegisterUserState.username)


async def register_hand_2(message: types.Message, state: FSMContext):
    """Функция register_hand_2. Ожидает ввод от пользователя."""
    await message.delete()
    username = message.text
    await state.update_data({"username": username})

    await message.answer("Придумайте пароль", reply_markup=KB)

    await state.set_state(RegisterUserState.password)


async def register_hand_3(message: types.Message, state: FSMContext):
    """Функция register_hand_3. Отправляет запрос с данными для регистрации нового пользователя."""
    context_data = await state.get_data()
    username = context_data.get("username")
    password = message.text

    data = {"username": username, "password": password, "telegram_id": message.from_user.id}
    status, response = await API_MANAGER.send_post(url="api/users/", json=data)

    if status == 201:
        txt = "Вы зарегистрированы"
    else:
        txt = "Что-то пошло не так. Попробуйте ещё раз"

    await message.answer(txt)
    await state.clear()

    await start_command(message)
