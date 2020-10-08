import asyncio
import threading
import time
from asyncio import FIRST_EXCEPTION

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
    print(f'{task_name} finished task')
    return [Photo.from_json(photo) for photo in photos_json]


async def main_wait():
    async with aiohttp.ClientSession() as session:
        tasks = [
            photos_by_album('t1', 1, session),
            photos_by_album('t2', 2, session),
            photos_by_album('t3', 3, session),
            photos_by_album('ta', 'a', session),
            photos_by_album('t4', 4, session)
        ]
        photos = []
        done, pending = await asyncio.wait(tasks,return_when=FIRST_EXCEPTION)
        for pending_task in pending:
            print(f'Cancel {pending_task}')
            pending_task.cancel()
        for done_task in done:
            try:
                result = done_task.result()
                photos.extend(result)
            except Exception as ex:
                print(repr(ex))
        print_photo_titles(photos)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(main_wait())
        loop.run_forever()
    finally:
        loop.close()
