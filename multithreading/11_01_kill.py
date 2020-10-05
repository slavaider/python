import multiprocessing
import time

from multithreading.functions_test import print_n

if __name__ == "__main__":
    print("start main")
    n = 50
    p = multiprocessing.Process(target=print_n, args=(n,))
    p.start()
    time.sleep(5)
    p.terminate()
    print("end main")
