import asyncio
import threading
import time

import aiohttp


class Photo:
    def __init__(self, album_id, photo_id, title, url, thumbnail):
        self.thumbnail = thumbnail
        self.url = url
        self.title = title
        self.photo_id = photo_id
        self.album_id = album_id

    @classmethod
    def from_json(cls, obj):
        return Photo(obj['albumId'], obj['id'], obj['title'], obj['url'], obj['thumbnailUrl'])


def print_photo_titles(photos):
    for photo in photos:
        print(photo.title, end='\n')


async def photos_by_album(task_name, album, session):
    if not isinstance(album, int):
        raise RuntimeError('Invalid album type')
    print(f'{task_name =}')
    url = f'https://jsonplaceholder.typicode.com/photos?albumId={album}'
    response = await session.get(url)
    photos_json = await response.json()

    sleeping_period = 3 if task_name == 't3' else 1
    print(f'{task_name} sleeping')
    await asyncio.sleep(sleeping_period)
    print(f'{task_name} finished sleeping')
    print(f'{task_name} finished task')
    return [Photo.from_json(photo) for photo in photos_json]


def get_coros(session):
    return [
        photos_by_album('t1', 1, session),
        photos_by_album('t2', 2, session),
        photos_by_album('t3', 3, session),
        photos_by_album('t4', 4, session)
    ]


def cancel_future(loop, future, after):
    def inner_cancel():
        print('\nsleeping before future cancel')
        time.sleep(after)
        print('\nfuture cancel')
        loop.call_soon_threadsafe(future.cancel)

    t = threading.Thread(target=inner_cancel)
    t.start()


async def main_gather_cancel_on_future():
    async with aiohttp.ClientSession() as session:
        future = asyncio.gather(*(get_coros(session)))
        cancel_future(asyncio.get_running_loop(), future, 3)
        try:
            print('\nawaiting future')
            result = await future
        except asyncio.exceptions.CancelledError as ex:
            print(repr(ex))


def cancel_task(tasks, after):
    def inner_cancel():
        time.sleep(after)
        for i, t in enumerate(tasks, start=1):
            print(f'Cancel {i} {t}')
            print(t.cancel())

    t = threading.Thread(target=inner_cancel)
    t.start()


async def main_gather_cancel_on_tasks():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(cor) for cor in get_coros(session)]
        future = asyncio.gather(*tasks)
        cancel_task(tasks, 2)
        try:
            print('\nawaiting future')
            result = await future
        except asyncio.exceptions.CancelledError as ex:
            print(repr(ex))


async def main_gather_return_exceptions():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(cor) for cor in get_coros(session)]
        future = asyncio.gather(*tasks, return_exceptions=True)
        cancel_task(tasks, 2)
        try:
            print('\nawaiting future')
            results = await future
            for result in results:
                if isinstance(result, asyncio.exceptions.CancelledError):
                    print(repr(result))
                else:
                    print_photo_titles(result)
        except Exception as ex:
            print(repr(ex))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        #  loop.create_task(main_gather_cancel_on_future())
        # loop.create_task(main_gather_cancel_on_tasks())
        loop.create_task(main_gather_return_exceptions())
        loop.run_forever()
    finally:
        loop.close()
