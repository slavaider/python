from threading import Thread

from multithreading.functions_test import print_n

if __name__ == "__main__":
    t1 = Thread(target=print_n, kwargs=dict(n=100, t="t1"), daemon=True)
    t1.start()
    print(input("what is ur name"))
    print("end_main")
