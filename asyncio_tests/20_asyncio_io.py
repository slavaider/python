import asyncio

import aiohttp

from multithreading.decorators_test import async_measure_time


async def download_site(url, session):
    async with session.get(url) as response:
        print(f'{response.content.total_bytes} from {url}')


@async_measure_time
async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.create_task(download_site(url, session))
            tasks.append(task)
        try:
            await asyncio.gather(*tasks, return_exceptions=True)
        except Exception as ex:
            print(repr(ex))


if __name__ == '__main__':
    sites = ['https://engineerspock.com', 'https://google.com'] * 80
    loop = asyncio.get_event_loop()
    loop.create_task(download_all_sites(sites))
    loop.run_forever()
