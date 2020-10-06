import asyncio


async def async_tick():
    print('Tick')
    await asyncio.sleep(1)
    print('Tock')
    return 'Tick-Tock'


async def main():
    t1 = asyncio.create_task(async_tick(), name='1')
    # same
    t2 = asyncio.ensure_future(async_tick())

    # await t1
    # await t2
    result = await asyncio.gather(t1, t2)

    print(f'Task {t1.get_name()}, done - {t1.done()}')
    print(f'{t2.get_name()}, done - {t2.done()}')
    
    for i in result:
        print(i)


if __name__ == '__main__':
    asyncio.run(main())
