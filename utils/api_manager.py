"""Модуль менеджера API."""

from typing import Any

import aiohttp

from config_data.config import URL_BACKEND_SERVER as url_from_config


class ApiManager:
    URL_BACKEND_SERVER = url_from_config

    @classmethod
    async def send_get(
        cls,
        params: dict = None,
        data: dict = None,
        headers: dict = None,
        url: str = "api/",
    ) -> tuple[int, Any]:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{cls.URL_BACKEND_SERVER}/{url}",
                data=data,
                params=params,
                headers=headers,
            ) as response:
                return response.status, await response.json()

    @classmethod
    async def send_post(
        cls,
        params: dict = None,
        data: dict = None,
        json: dict = None,
        url: str = "api/",
    ) -> tuple[int, Any]:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=f"{cls.URL_BACKEND_SERVER}/{url}",
                json=json,
                data=data,
                params=params,
            ) as response:
                return response.status, await response.json()
                # return response

    @classmethod
    async def send_delete(
        cls,
        params: dict = None,
        data: dict = None,
        json: dict = None,
        url: str = "api/",
    ) -> int:
        async with aiohttp.ClientSession() as session:
            async with session.delete(
                url=f"{cls.URL_BACKEND_SERVER}/{url}",
                json=json,
                data=data,
                params=params,
            ) as response:
                return response.status
                # return response

    @classmethod
    async def send_patch(
        cls,
        params: dict = None,
        data: dict = None,
        json: dict = None,
        url: str = "api/",
    ) -> int:
        async with aiohttp.ClientSession() as session:
            async with session.patch(
                url=f"{cls.URL_BACKEND_SERVER}/{url}",
                json=json,
                data=data,
                params=params,
            ) as response:
                return response.status
