
# import asyncio
# import aiohttp
#
# # Import the pprint module to print the JSON response in a readable format
# # This is a built-in module, so it does not need to be installed
# from pprint import pprint
#
#
# async def main():
#     # data = {'username': 'qwe', 'password': 'ghjk', 'telegram_id': 5203073246}
#     data = {
#         "username": "string2",
#         "password": "string1",
#         "telegram_id": 5203073246
#     }
#     # Create a session using the async with statement
#     async with aiohttp.ClientSession() as session:
#         # Make a POST request using the session.post() method
#         async with session.post("http://0.0.0.0:8000/api/users", json=data) as response:
#         # async with session.get("http://0.0.0.0:8000/api/users/me") as response:
#             # Print the status code and the response text
#             print(f"Status: {response.status}")
#             # pprint(await response.json())
#
#
# # Run the main coroutine
# # url = "https://api.slingacademy.com/v1/sample-data/products"
# asyncio.run(main())


# import asyncio
# import logging
# import sys
# from os import getenv
#
# from aiogram import Bot, Dispatcher, Router, types
# from aiogram.enums import ParseMode
# from aiogram.filters import CommandStart
# from aiogram.types import Message
# from aiogram.utils.markdown import hbold
# from aiogram.client.session.aiohttp import AiohttpSession
# from aiogram.client.telegram import TelegramAPIServer
#
# # Bot token can be obtained via https://t.me/BotFather
# TOKEN = "6006361719:AAGaqur4GbDnd180I_Nilv6GPcm9MdRM8vA"
#
# # All handlers should be attached to the Router (or Dispatcher)
# dp = Dispatcher()
#
#
# @dp.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
#     """
#     This handler receives messages with `/start` command
#     """
#     # Most event objects have aliases for API methods that can be called in events' context
#     # For example if you want to answer to incoming message you can use `message.answer(...)` alias
#     # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
#     # method automatically or call API method directly via
#     # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
#     await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
#
#
# @dp.message()
# async def echo_handler(message: types.Message) -> None:
#     """
#     Handler will forward receive a message back to the sender
#
#     By default, message handler will handle all message types (like a text, photo, sticker etc.)
#     """
#     try:
#         # Send a copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")
#
#
# async def main() -> None:
#     session = AiohttpSession(
#         # api=TelegramAPIServer.from_base('https://tgrasp.co')  # your address
#         # api=TelegramAPIServer.from_base('http://0.0.0.0:8000')  # your address
#     )
#
#     # Initialize Bot instance with a default parse mode which will be passed to all API calls
#     bot = Bot(TOKEN, parse_mode=ParseMode.HTML, session=session)
#
#     # And the run events dispatching
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())

import requests
array = '{"chat_id": "' + chat_id + '", "text": "Test Buttons", "reply_markup" : { "inline_keyboard" : [[ { "text" : "web", "url" :"google.es"}]]}}'
data3 = json.loads(array)

print(array)
url = f'https://api.telegram.org/bot{token}/sendMessage'
response = requests.get(url, params=data3)
print(response.json())