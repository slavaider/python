import threading
import time

should_stop = False


def print_n(n, t=""):
    global should_stop
    print(f"start {t}")
    for i in range(1, n + 1):
        if should_stop:
            print("\nstop!")
            return
        print(i)
    print(f"end {t}")


if __name__ == '__main__':
    print("start main")
    n = 50000
    t = threading.Thread(target=print_n, args=(n,))
    t.start()
    time.sleep(0.2)
    should_stop = not should_stop
    time.sleep(1)
    print("end main")
