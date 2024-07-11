"""Модуль схема пользователя."""

from pydantic import BaseModel

from objects.token import Token


class User(BaseModel):
    telegram_id: int = None
    username: str = None
    full_name: str = None
    first_name: str = None
    last_name: str = None
    token: Token = None

    def __del__(self) -> None:
        self.telegram_id = None
        self.username = None
        self.full_name = None
        self.first_name = None
        self.last_name = None
        self.token = None


user_obj = User()
