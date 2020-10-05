import concurrent.futures
import time
from multithreading.functions_test import div

if __name__ == "__main__":
    print("started main")
    futures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        futures.append(executor.submit(div, 5, 25))
        futures.append(executor.submit(div, 3, 25))
        while futures[0].running() and futures[1].running():
            print(".", end="")
            time.sleep(0.5)
        print(futures[0].result())
        print(futures[1].result())
    print("After with block")

    # executor = concurrent.futures.ThreadPoolExecutor(2)
    # executor.submit(div, 5, 25)
    # executor.submit(print_n, 3, 25)
    # executor.shutdown(wait=False)
    print("end main")
