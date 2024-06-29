"""Модуль хранения данных (состояний) пользователя."""
from aiogram.fsm.state import State, StatesGroup


class RegisterUserState(StatesGroup):
    """Класс RegisterUserState. Хранит информацию и данные вводимые пользователем."""
    username = State()
    password = State()


class LoginUserState(StatesGroup):
    """Класс RegisterUserState. Хранит информацию и данные вводимые пользователем."""
    username = State()
    password = State()


class CreateHabitState(StatesGroup):
    """Класс RegisterUserState. Хранит информацию и данные вводимые пользователем."""
    name = State()
    description = State()
    alert_time = State()


class EditHabitState(StatesGroup):
    name = State()
    description = State()
    alert_time = State()



