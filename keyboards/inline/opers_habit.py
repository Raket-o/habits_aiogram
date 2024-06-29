"""Модуль создания клавиатуры (работа с пользователем)."""
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def habit_opers_buttons(habit_id: int) -> InlineKeyboardMarkup:
    """
    Функция создания клавиатуры работа с пользователем.
    :return: InlineKeyboardMarkup
    """
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Редактировать", callback_data=f"habit_edit_hand={habit_id}")
    keyboard_builder.button(text="Удалить", callback_data=f"habit_del_hand={habit_id}")
    keyboard_builder.button(text="Вернуться к списку", callback_data=f"main_menu_hand_1")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()