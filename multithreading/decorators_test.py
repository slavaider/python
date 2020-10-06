from functools import wraps
import time


def async_measure_time(func):
    @wraps(func)
    async def wrap(*args, **kwargs):
        start = time.perf_counter()
        result = await func(*args, **kwargs)
        stop = time.perf_counter() - start
        print(f"{func} Execution time was {stop:0.6f}s")
        return result

    return wrap


def measure_time(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        stop = time.perf_counter() - start
        print(f"{func} Execution time was {stop:0.6f}s")
        return result

    return wrap
