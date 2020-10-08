import asyncio
import threading


async def fetch_dock(doc):
    await asyncio.sleep(1)  # emulation
    return doc


async def get_docks(docs, token):
    pages = []
    for cur in docs:
        if token.is_set():
            break
        dock = await fetch_dock(cur)
        for page in dock:
            pages.append(page)
    return pages


def get_response(token):
    reply = input('y/n')
    if reply == 'y':
        token.set()


async def main():
    token = threading.Event()
    task = asyncio.create_task(get_docks(['doc1', 'doc2', 'doc3'], token))
    t = threading.Thread(target=get_response, args=(token,))
    t.start()
    res = await task
    for doc in res:
        print(doc)


if __name__ == '__main__':
    asyncio.run(main())
