import time

from multithreading.decorators_test import measure_time


@measure_time
def print_n(n, t=""):
    print(f"start {t}")
    for i in range(1, n + 1):
        print(i)
    print(f"end {t}")


def div(divisor, limit):
    print(f"start {divisor}")
    result = 0
    for x in range(1, limit):
        if x % divisor == 0:
            result += x
        time.sleep(0.2)
    print(f"end {divisor}", end="\n")
    return result
