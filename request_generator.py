import requests
import threading
import aiohttp
import asyncio
from contextlib import suppress
import nest_asyncio
from ratelimit import limits, sleep_and_retry


nest_asyncio.apply()


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
        if self.generate_type == 'thread':
            self.threading_requests()
            
    async def generate_async(self):
        # loop = asyncio.new_event_loop()
        # loop.create_task(self.make_async_thread(loop))
        # loop.run_forever()
        loop = asyncio.get_event_loop()
        asyncio.ensure_future(self.make_async_thread(loop))
        loop.run_until_complete(self.make_async_thread(loop))

    def make_linear_thread(self):
        while True:
            requests.get(self.target_url)

    # @sleep_and_retry
    # @limits(calls=rate_limit, period=1)
    async def send_request(self, session):
        await session.get(self.target_url)

    async def make_async_thread(self, loop):
        while True:
            async with aiohttp.ClientSession(loop=loop) as session:
                await self.send_request(session)

    def threading_requests(self):
        for t in range(self.threads):
            my_thread = threading.Thread(target=self.make_thread, daemon=True)
            my_thread.start()

    def make_thread(self):
        while True:
            thread = threading.Thread(target=self.make_linear_thread, daemon=True)
            thread.start()
