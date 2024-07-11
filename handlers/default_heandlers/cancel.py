"""Модуль сброса состояние пользователя."""
import logging

from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from handlers.default_heandlers.start import start_command


async def cancel_handler_1(message: Message, state: FSMContext) -> None:
    """
    Функция weekend. Команда /cancel запускает данную функцию.
    Функция сбрасывает состояние пользователя.
    """
    logging.info("cancel_handler")
    current_state = await state.get_state()
    if current_state is None:
        await message.answer(
            "Отмена",
            reply_markup=ReplyKeyboardRemove(),
        )

    logging.info("Cancelling state %r", current_state)
    await state.clear()
    await message.answer(
        "Отмена",
        reply_markup=ReplyKeyboardRemove(),
    )

    await start_command(message)
