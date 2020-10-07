import asyncio


async def fetch_dock(doc):
    await asyncio.sleep(1)  # emulation
    return doc


async def get_docks(docs):
    for cur in docs:
        dock = await fetch_dock(cur)
        for page in dock:
            await asyncio.sleep(1)
            yield page


async def main():
    async for page in get_docks(['doc1', 'doc2']):
        print(f'finally {page}')


if __name__ == '__main__':
    asyncio.run(main())
