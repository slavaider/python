import requests
from requests import HTTPError
from requests.adapters import HTTPAdapter
from requests.exceptions import Timeout

if __name__ == '__main__':
    try:
        a = requests.get(r"https://jsonplaceholder.typicode.com/todos/", params="userId=1")
        d = list(a.json())
        print(d)
        print(type(d))
        print(a.status_code)
    except HTTPError as error:
        print(f"{error}")
    print()

    for url in [r"https://jsonplaceholder.typicode.com/todos/", r"https://jsonplaceholder.typicode.com/posts/"]:
        try:
            print(1)
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as error:
            print(f"{error}")
        except Exception as error:
            print(f"{error}")
        else:
            print("Connected success")
    print()

    r_q = requests.get(r"https://api.github.com/")
    print(r_q.headers["content-type"])
    response1 = requests.post(r"https://httpbin.org/post", json={"a": 1, "b": 2})
    print(response1.json())
    response2 = requests.get(r"https://httpbin.org/get")
    print(response2.json())
    print()

    try:
        auth = requests.get(r"https://jsonplaceholder.typicode.com/todos/", timeout=1)
    except Timeout as err:
        print(f"{err}")
    adapter1 = HTTPAdapter(max_retries=3)
    with requests.session() as session:
        # session.auth = "123"
        session.mount("https://api.google.com", adapter1)
        a = session.get("https://api.google.com")
        print(a.text)
