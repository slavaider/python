import asyncio

from multithreading.decorators_test import async_measure_time
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
    print(f'{task_name =}')
    url = f'https://jsonplaceholder.typicode.com/photos?albumId={album}'
    response = await session.get(url)
    photos_json = await response.json()
    return [Photo.from_json(photo) for photo in photos_json]


@async_measure_time
async def main():
    # async with aiohttp.ClientSession() as session:
    #     photos = await photos_by_album('Task 1', 3, session)
    #     print_photo_titles(photos)

    async with aiohttp.ClientSession() as session:
        photos_in_albums = await asyncio.gather(*(photos_by_album(f'Task {i + 1}', album, session)
                                                  for i, album in enumerate(range(2, 30))))
        photos_count = sum([len(cur) for cur in photos_in_albums])
        print(photos_count)


if __name__ == '__main__':
    asyncio.run(main())
    # Event loop is closed баг из aiohttp

    loop = asyncio.get_event_loop()
    try:
        loop.create_task(main())
        loop.run_forever()
    finally:
        loop.close()
