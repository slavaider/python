import requests

from multithreading.decorators_test import measure_time


def download_site(url, session):
    with session.get(url) as response:
        print(f'{len(response.content)} from {url}')


@measure_time
def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == '__main__':
    sites = ['https://engineerspock.com', 'https://google.com'] * 20
    download_all_sites(sites)
