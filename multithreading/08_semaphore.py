import concurrent.futures
import random
import threading
import time


def connection_guard(semaphore, reached_max):
    while True:
        print(f"guard = {semaphore._value}")
        time.sleep(1.5)
        if semaphore._value == 0:
            reached_max.set()
            print("guard reached max")
            time.sleep(2)
            reached_max.clear()


def work(semaphore):
    time.sleep(random.randint(5, 10))
    print("release 1 connection")
    semaphore.release()


def connect(semaphore, reached_max):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
        while True:
            counter = 10
            while not reached_max.is_set():
                print(f"connection n = {counter}")
                semaphore.acquire()
                counter += 1
                ex.submit(work, semaphore)
                time.sleep(0.8)
            time.sleep(5)


if __name__ == "__main__":
    max_count = 10
    reached_max = threading.Event()
    semaphore = threading.Semaphore(max_count)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(connection_guard, semaphore, reached_max)
        executor.submit(connect, semaphore, reached_max)
