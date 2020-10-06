import asyncio
import time


async def async_tick():
    await asyncio.sleep(1)
    return 'Tick'


async def async_tock():
    await asyncio.sleep(2)
    return 'Tock'


async def main():
    start = time.perf_counter()
    t1 = asyncio.create_task(async_tick())
    t2 = asyncio.create_task(async_tock())
    # results = await asyncio.gather(t1, t2)
    for i, t in enumerate(asyncio.as_completed((t1, t2)), start=1):
        result = await t
        elapsed = time.perf_counter() - start
        print(f'Executed in {elapsed:0.2f} s')
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
