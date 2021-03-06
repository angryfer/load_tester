from request_generator import RequestGenerator
import asyncio
from monitoring import Monitor


class LoadTester():
    def __init__(self):
        self.config = './config.json'
        self.ammo = 'ammo.txt'
        self.workers = 1
        self.time = 30
        self.rps = 10
        self.url = 'http://127.0.0.1:5000/one'
        self.type = 'thread'

    async def start(self):
        self.generator = RequestGenerator(self.url, self.type)
        await self.generator.generate()


if __name__ == '__main__':
    load = LoadTester()

    asyncio.run(load.start())
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(load.start())
    while True:
        print(load.generator.monitoring.check_rps())
