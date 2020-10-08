import asyncio


class MyError(Exception):
    pass


async def my_sleep(sec):
    print(f'Task {sec}')
    await asyncio.sleep(sec)
    print(f'Task {sec} finished sleeping')
    if sec == 5:
        raise MyError('5 is forbidden')
    print(f'Slept for {sec}')


async def main_cancel_tasks():
    tasks = [asyncio.create_task(my_sleep(sec)) for sec in [2, 5, 7]]
    sleepers = asyncio.gather(*tasks)
    try:
        await sleepers
    except MyError:
        print('Fatal Error')
        for t in tasks:
            t.cancel()
    finally:
        await asyncio.sleep(5)


async def main_cancel_future():
    sleepers = asyncio.gather(*[my_sleep(secs) for secs in [2, 5, 7]])
    try:
        await sleepers
    except MyError:
        print('Fatal Error')
        sleepers.cancel()
    finally:
        await asyncio.sleep(5)


if __name__ == '__main__':
    asyncio.run(main_cancel_tasks())
