import aiohttp
import asyncio
import time
import json
from Fetch import Fetcher as fetcher


async def fetch_url():
    start = time.time()
    print(f"started at {time.strftime('%X')}")
    getRequest = await fetcher.get('https://httpbin.org/get')
    deleteRequest = await fetcher.delete('https://httpbin.org/delete')
    jsonData ={
    "id": "30",
    "name": "Someone"
    }
    postRequest = await fetcher.post('https://httpbin.org/post',jsonData)
    print(postRequest)
    end = time.time()
    print(f"finished at {time.strftime('%X')}")
    print(f"total time execution : {round(int(end - start))}") 

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_url())