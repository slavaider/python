import asyncio
import time
from multithreading.decorators_test import measure_time
from multithreading.decorators_test import async_measure_time


@measure_time
def main():
    for _ in range(3):
        print('Tick')
        time.sleep(1)
        print('Tock')


async def async_tick(num: int = 1):
    print('Tick')
    num += 1
    await asyncio.sleep(1)
    print(num)
    print('Tock')


@async_measure_time
async def async_main():
    await asyncio.gather(async_tick(), async_tick(), async_tick())


if __name__ == '__main__':
    # main()
    asyncio.run(async_main())
