import aiohttp
import asyncio
import time
import requests
import json

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    start = time.time()
    print(f"started at {time.strftime('%X')}")

    async with aiohttp.ClientSession() as session:
        data = await fetch(session, 'https://jsonplaceholder.typicode.com/posts')
        for x in data:
            print("title :", x['title'])

    end = time.time()
    print(f"finished at {time.strftime('%X')}")
    print(f"total time execution : {round(int(end - start))}") 

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())