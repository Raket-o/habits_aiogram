from pydantic import BaseModel


class Token(BaseModel):
    token: str = None

    def __str__(self):
        return self.token

    def __repr__(self):
        return self.token

    def __del__(self):
        self.token = None
        # print('Object destroyed')

    # def __enter__(self):
    #     return self
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     print("bye")
    #     del self.token


token_obj = Token()
