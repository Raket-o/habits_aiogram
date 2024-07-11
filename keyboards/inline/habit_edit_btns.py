"""Модуль создания клавиатуры."""
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def edit_habit_buttons(habit_id: int) -> InlineKeyboardMarkup:
    """
    Функция создания клавиатуры.
    :return: InlineKeyboardMarkup
    """
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Название", callback_data=f"edit_name_hand={habit_id}")
    keyboard_builder.button(text="Описание", callback_data=f"edit_description_hand={habit_id}")
    keyboard_builder.button(text="Время оповещения", callback_data=f"edit_alert_time_hand={habit_id}")
    keyboard_builder.button(text="Вернуться к списку", callback_data=f"main_menu_hand_1")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
