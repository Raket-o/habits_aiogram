from pydantic import BaseModel

from objects.token import Token


class User(BaseModel):
    telegram_id: int = None
    username: str = None
    full_name: str = None
    first_name: str = None
    last_name: str = None
    token: Token = None

    def __del__(self):
        # del self
        self.telegram_id = None
        self.username = None
        self.full_name = None
        self.first_name = None
        self.last_name = None
        self.token = None
        # print('Object destroyed')

    # def __enter__(self):
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     print("bye")
    #     del self.telegram_id
    #     del self.username
    #     del self.full_name
    #     del self.first_name
    #     del self.last_name
    #     del self.token


user_obj = User()
