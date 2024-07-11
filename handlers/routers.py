"""Модуль регистрации хендлеров пользователя."""
from aiogram import F, Router
from aiogram.filters import Command, CommandStart

from handlers.custom_handlers.actioins_users.register import register_hand_1, register_hand_2, register_hand_3
from handlers.custom_handlers.actioins_users.login import login_hand_1, login_hand_2, login_hand_3

from handlers.custom_handlers.actioins_users.logout import logout_hand_1

from handlers.custom_handlers.actioins_users.habit_create import (
    create_habit_hand_1,
    create_habit_hand_2,
    create_habit_hand_3,
    create_habit_hand_4
)

from handlers.default_heandlers.cancel import cancel_handler_1
from handlers.default_heandlers.start import start_command
from states.states import CreateHabitState, RegisterUserState, LoginUserState, EditHabitState

from handlers.custom_handlers.actioins_users.habit_get_detail import get_detail_habit_hand_1

from handlers.custom_handlers.actioins_users.main_menu import main_menu_hand_1

from handlers.custom_handlers.actioins_users.habit_del import del_habit_hand_1

from handlers.custom_handlers.actioins_users.habit_edit import (
    edit_habit_hand,
    edit_name_habit_hand_1,
    edit_name_habit_hand_2,
    edit_description_habit_hand_1,
    edit_description_habit_hand_2,
    edit_alert_time_habit_hand_1,
    edit_alert_time_habit_hand_2,
)

from handlers.custom_handlers.actioins_users.habit_completed import habit_comp_1, habit_did_not_comp_1


def register_routers(router: Router):
    """
    Функция register_routers. Собирает хендлеры в основной router.
    """
    router.message.register(start_command, CommandStart())
    router.callback_query.register(start_command, F.data.startswith("start_command="))

    router.callback_query.register(register_hand_1, F.data == "register_hand_1")
    router.message.register(register_hand_2, RegisterUserState.username)
    router.message.register(register_hand_3, RegisterUserState.password)

    router.callback_query.register(login_hand_1, F.data == "login_hand_1")
    router.message.register(login_hand_2, LoginUserState.username)
    router.message.register(login_hand_3, LoginUserState.password)

    router.callback_query.register(logout_hand_1, F.data == "logout_hand_1")

    router.callback_query.register(create_habit_hand_1, F.data == "create_habit_hand_1")
    router.message.register(create_habit_hand_2, CreateHabitState.name)
    router.message.register(create_habit_hand_3, CreateHabitState.description)
    router.message.register(create_habit_hand_4, CreateHabitState.alert_time)

    router.callback_query.register(cancel_handler_1, F.data == "cancel_hand_1")
    router.message.register(cancel_handler_1, Command('cancel_hand_1'))

    router.callback_query.register(get_detail_habit_hand_1, F.data.startswith("habit_id="))

    router.callback_query.register(main_menu_hand_1, F.data == "main_menu_hand_1")

    router.callback_query.register(del_habit_hand_1, F.data.startswith("habit_del_hand="))

    router.callback_query.register(edit_habit_hand, F.data.startswith("habit_edit_hand="))
    router.callback_query.register(edit_name_habit_hand_1, F.data.startswith("edit_name_hand="))
    router.message.register(edit_name_habit_hand_2, EditHabitState.name)

    router.callback_query.register(edit_description_habit_hand_1, F.data.startswith("edit_description_hand="))
    router.message.register(edit_description_habit_hand_2, EditHabitState.description)

    router.callback_query.register(edit_alert_time_habit_hand_1, F.data.startswith("edit_alert_time_hand="))
    router.message.register(edit_alert_time_habit_hand_2, EditHabitState.alert_time)

    router.callback_query.register(habit_comp_1, F.data.startswith("completed_habit="))
    router.callback_query.register(habit_did_not_comp_1, F.data.startswith("did_not_completed_habit="))
