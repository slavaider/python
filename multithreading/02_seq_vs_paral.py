from threading import Thread

from multithreading.decorators_test import measure_time
from multithreading.functions_test import print_n
import time


@measure_time
def run_in_parallel(n):
    t1 = Thread(target=print_n, kwargs=dict(n=n, t='t1'), daemon=True)
    t2 = Thread(target=print_n, kwargs=dict(n=n, t='t2'), daemon=True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


@measure_time
def run_in_seq(n):
    print_n(n)
    print_n(n)


if __name__ == "__main__":
    print("started main")
    run_in_parallel(10)
    run_in_seq(10)
    print("stop main")
