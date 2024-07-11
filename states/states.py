"""Модуль хранения данных (состояний) пользователя."""

from aiogram.fsm.state import State, StatesGroup


class RegisterUserState(StatesGroup):
    """Класс RegisterUserState. Хранит информацию состояние."""

    username = State()
    password = State()


class LoginUserState(StatesGroup):
    """Класс LoginUserState. Хранит информацию состояние."""

    username = State()
    password = State()


class CreateHabitState(StatesGroup):
    """Класс CreateHabitState. Хранит информацию состояние."""

    name = State()
    description = State()
    alert_time = State()


class EditHabitState(StatesGroup):
    """Класс EditHabitState. Хранит информацию состояние."""

    name = State()
    description = State()
    alert_time = State()
