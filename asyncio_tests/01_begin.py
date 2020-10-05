import asyncio
import time

from multithreading.decorators_test import measure_time


async def tick(num):
    print('Tick')
    num += 1
    await asyncio.sleep(1)
    print(num)
    print('Tock')


# @measure_time
# def main():
#     for _ in range(3):
#         tick()

async def main():
    await asyncio.gather(tick(1), tick(1), tick(1))


if __name__ == '__main__':
    asyncio.run(main())
