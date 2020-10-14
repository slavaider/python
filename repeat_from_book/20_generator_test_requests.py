import requests


def gen_from_urls(func_urls: tuple) -> tuple:
    for response in (requests.get(func_url) for func_url in func_urls):
        yield len(response.content), response.status_code, response.url


if __name__ == '__main__':
    urls = ('http://headfirstlabs.com', 'http://oreilly.com', 'http://twitter.com')
    for resp_len, status, url in gen_from_urls(urls):
        print(resp_len, '->', status, '->', url)
