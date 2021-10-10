import requests
import threading
import aiohttp
import asyncio
from contextlib import suppress
import nest_asyncio


nest_asyncio.apply()
# __import__('IPython').embed()


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
            await self.generate_async()
            
    async def generate_async(self):
        # loop = asyncio.new_event_loop()
        # loop.create_task(self.make_async_thread())
        # loop.run_forever()
        loop = asyncio.get_event_loop()
        asyncio.ensure_future(self.make_async_thread(loop))
        loop.run_until_complete(self.make_async_thread(loop))

    def make_linear_thread(self):
        while True:
            requests.get(self.target_url)

    async def make_async_thread(self, loop):
        while True:
            async with aiohttp.ClientSession(loop=loop) as session:
                await session.get(self.target_url)
