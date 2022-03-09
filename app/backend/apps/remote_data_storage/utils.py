import asyncio
from typing import List, Coroutine, Any

import aiohttp
from pydantic import AnyHttpUrl, parse_obj_as

from app.backend.apps.remote_data_storage.models import Item
from app.backend.settings import settings


class DataAggregator:
    """
    Async data fetcher from remote services.
    """
    timeout_delay = aiohttp.ClientTimeout(settings.REQUEST_TIMEOUT_SECONDS)

    def __init__(self, session: aiohttp.ClientSession):
        self.session = session

    async def fetch_data(self, urls: List[AnyHttpUrl]) -> List[Item]:
        """
        Fetch data from a lot of remote services in ordering by id.
        """
        items_groups = [self.__get_sorted_items(url) for url in urls]
        return await self.__prepare_data_set(items_groups)

    async def __get_sorted_items(self, source_url: AnyHttpUrl) -> List[Item]:
        try:
            async with self.session.get(source_url, timeout=self.timeout_delay, raise_for_status=True) as response:
                response = parse_obj_as(List[Item], await response.json())
                return await self.sort_items_by_id(response)
        except (asyncio.TimeoutError, aiohttp.ClientResponseError):
            return []

    async def __prepare_data_set(self, items_groups: List[Coroutine[Any, Any, List[Item]]]) -> List[Item]:
        data = []
        for items in asyncio.as_completed(items_groups):
            data = await self.sort_items_by_id(await items + data)

        return data

    # TODO: rename from items to real data model name not abstract
    @staticmethod
    async def sort_items_by_id(data: List[Item]) -> List[Item]:
        """
        "items" means Item SQLModel.
        """
        return sorted(data, key=lambda x: x.id)
