import asyncio

import aiofiles


def read_large_file():
    with open(r'../files/json_tests.txt', 'r') as file:
        return file.read()


async def async_read_large_file():
    async with aiofiles.open(r'../files/json_tests.txt', 'r') as file:
        return await file.read()


def count_words(text):
    return len(text.split(' '))


def main():
    text = read_large_file()
    print(count_words(text))


async def async_main():
    text = await async_read_large_file()
    print(count_words(text))


if __name__ == '__main__':
    asyncio.run(async_main())
    main()
