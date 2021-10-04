import requests
import threading
import aiohttp
import asyncio


class RequestGenerator():

    def __init__(self, target_url, generate_type):
        self.target_url = target_url
        self.rate_limit = 100
        self.threads = 1
        self.generate_type = generate_type

    async def generate(self):
        if self.generate_type == 'linear':
            self.make_linear_thread()
        if self.generate_type == 'async':
            await self.make_async_thread()
            # loop = asyncio.get_event_loop()
            # loop.run_until_complete(self.make_async_thread())
            # asyncio.run(self.make_async_thread)

    def make_linear_thread(self):
        while True:
            requests.get(self.target_url)

    async def make_async_thread(self):
        while True:
            async with aiohttp.ClientSession() as session:
                await session.get(self.target_url)
