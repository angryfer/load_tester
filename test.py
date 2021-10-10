import asyncio, aiohttp, argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", type=str)
parser.add_argument("--concurrency", default=16, type=int)
parser.add_argument("--timeout", default=5, type=int)
args = parser.parse_args()


async def send_request(url):
    while True:
        try:
            async with session.get(url) as resp:
                if resp.status != 200:
                    print('Ошибка сервера')
        except aiohttp.client_exceptions.ServerTimeoutError:
            print('таймаут')


async def main():
    global session
    session = aiohttp.ClientSession(
        timeout=aiohttp.ClientTimeout(args.timeout)
    )

    tasks = [
        send_request(args.url)
        for i
        in range(args.concurrency)
    ]
    await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())