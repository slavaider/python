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
    print(f'{task_name =}')
    url = f'https://jsonplaceholder.typicode.com/photos?albumId={album}'
    response = await session.get(url)
    photos_json = await response.json()
    return [Photo.from_json(photo) for photo in photos_json]


async def download_albums(albums):
    async with aiohttp.ClientSession() as session:
        for album in albums:
            if not isinstance(album, int):
                raise RuntimeError('Invalid album type')
            yield await photos_by_album(f'Task {album}', album, session)


async def main():
    try:
        async  for photos in download_albums([1, 2, 3, '4']):
            print_photo_titles(photos)
    except Exception as ex:
        print(repr(ex))


if __name__ == '__main__':
    asyncio.run(main())
    print('Main ended')
