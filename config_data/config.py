"""Модуль конфиг для проверки создано ли окружение."""

import os

from dotenv import find_dotenv, load_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
START_MESSAGE = os.getenv("START_MESSAGE")
URL_BACKEND_SERVER = os.getenv("URL_BACKEND_SERVER")

DEFAULT_COMMANDS = ("start", "Запустить бота")
