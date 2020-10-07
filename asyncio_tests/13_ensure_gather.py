import asyncio

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
    return [Photo.from_json(photo) for photo in photos_json]


async def download_albums(albums):
    photos = []
    async with aiohttp.ClientSession() as session:
        for album in albums:
            photos.extend(await photos_by_album(f'Task {album}', album, session))
    return photos


async def main():
    task = asyncio.create_task(download_albums([1, 2, 'a', 4]))
    try:
        await task
    except Exception as ex:
        print(repr(ex))


async def handle_result(future):
    print(future.result())


async def main1():
    task = asyncio.create_task(download_albums([1, 2, 'a', 4]))
    task.add_done_callback(handle_result)
    await asyncio.sleep(2)


async def main_gather():
    async with aiohttp.ClientSession() as session:
        tasks = [
            photos_by_album('t1`', 1, session),
            photos_by_album('t2`', 2, session),
            photos_by_album('t3`', 3, session),
            photos_by_album('t4`', 4, session)
        ]
        photos = []
        results = await asyncio.gather(*tasks, return_exceptions=True)
        for res in results:
            if isinstance(res, Exception):
                print(repr(res))
            else:
                photos.extend(res)
        print_photo_titles(photos)


if __name__ == '__main__':
    # asyncio.run(main())
    # asyncio.run(main1())
    asyncio.run(main_gather())
    print('Main ended')
