

from functools import wraps
import time
import math
from timeit import default_timer as timer


def hello_w1():
    def internal1():
        print("hello w")
    return internal1


def say(func):
    func()


def log_d(func):
    def wrap():
        print(f'Calling func {func}')
        func()
        print(f'{func} end')
    return wrap


hello2 = hello_w1()
# hello2()

# say(hello_w)


def count_time(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        end = timer()
        print(f'{func.__name__} took {round(end - start,6)} seconds')
    return wrap


@count_time
def hello():
    time.sleep(3)
    print("Hello w")


hello()
