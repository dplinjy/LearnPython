# -*- encoding: utf-8 -*-
"""
@File    : simpletest.py
@Time    : 2020/1/18 20:30
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import aiohttp
import asyncio

# ------------------------------------------------------------------------
# for single request
# async def main():
#     async with aiohttp.request('GET', 'https://api.github.com/events') as resp:
#         json = await resp.json()
#         print(json)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

# ------------------------------------------------------------------------
# for multiple requests
# async def main():
#     tasks = []
#     [tasks.append(fetch('https://api.github.com/events?a={}'.format(i))) for i in range(10)]
#     await asyncio.wait(tasks)
#
#
# async def fetch(url):
#     async with aiohttp.request('GET', url) as resp:
#         json = await resp.json()
#         print(json)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())


# ------------------------------------------------------------------------
# multiple requests, in the meanwhile, restricting number of requests
async def main(pool):
    tasks = []
    sem = asyncio.Semaphore(pool)  # restrict number of requests
    [tasks.append(control_sem(sem, 'https://pai.github.com/events?a={}'.format(i))) for i in range(10)]
    await asyncio.wait(tasks)


async def control_sem(sem, url):  # 限制信号量
    async with sem:
        await fetch(url)


async def fetch(url):
    async with aiohttp.request('GET', url) as resp:
        json = await resp.json()
        print(json)


loop = asyncio.get_event_loop()
loop.run_until_complete(main(pool=2))




