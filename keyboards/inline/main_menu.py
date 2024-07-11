"""Модуль создания клавиатуры."""
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu_buttons(tpl_habits: tuple = None) -> InlineKeyboardMarkup:
    """
    Функция создания клавиатуры.
    :return: InlineKeyboardMarkup
    """
    keyboard_builder = InlineKeyboardBuilder()

    if tpl_habits:
        for habit in tpl_habits:
            keyboard_builder.button(text=f"{habit[1]}", callback_data=f"habit_id={habit[0]}")

    keyboard_builder.button(text="Записать привычку", callback_data="create_habit_hand_1")
    keyboard_builder.button(text="Выйти", callback_data="logout_hand_1")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
