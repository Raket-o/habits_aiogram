"""Модуль создания клавиатуры."""
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def greeting_buttons() -> InlineKeyboardMarkup:
    """
    Функция создания клавиатуры.
    :return: InlineKeyboardMarkup
    """
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Зарегистрироваться", callback_data="register_hand_1")
    keyboard_builder.button(text="Войти", callback_data="login_hand_1")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
