import concurrent.futures
from multithreading.functions_test import div

if __name__ == "__main__":
    print("started main")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        result_map = executor.map(div, (5, 3), (25, 25))
        for i in result_map:
            print(f"{i=}")
    print("end main")
