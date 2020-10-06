import asyncio


async def async_tick():
    print('Tick')
    await asyncio.sleep(1)
    print('Tock')
    loop = asyncio.get_running_loop()
    if loop.is_running():
        print('Loop is running')


async def async_main():
    awaitable_obj = asyncio.gather(async_tick(), async_tick(), async_tick())
    for task in asyncio.all_tasks():
        print(task)
    await awaitable_obj


if __name__ == '__main__':
    # coroutine = async_main()
    # print(coroutine)

    # asyncio.run(async_main())

    loop = asyncio.get_event_loop()
    try:
        # loop.create_task(async_main())
        # loop.run_forever()
        loop.run_until_complete(async_main())
        print('coroutine has finished')
    except KeyboardInterrupt:
        print('Manually closed program')
    finally:
        loop.close()
        print(f'loop is closed = {loop.is_closed()}')
