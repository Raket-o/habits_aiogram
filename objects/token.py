"""Модуль схема токена."""

from pydantic import BaseModel


class Token(BaseModel):
    token: str = None

    def __str__(self) -> str:
        return self.token

    def __repr__(self) -> str:
        return self.token

    def __del__(self) -> None:
        self.token = None


token_obj = Token()
