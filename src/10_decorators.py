import time
from functools import wraps
from timeit import default_timer as timer


def say(func):
    func()


def log_decorator_of_function(func):
    def wrap():
        print(f'Calling func {func}')
        func()
        print(f'{func} end')

    return wrap


def count_time(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        end = timer()
        print(f'{func.__name__} took {round(end - start, 6)} seconds')

    return wrap


@log_decorator_of_function
@count_time
def hello_function():
    time.sleep(3)
    print("Hello world")


if __name__ == '__main__':
    # wrap decorator
    say(hello_function)
    hello_function()
