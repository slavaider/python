import threading
import time


class print_nums:
    def __init__(self, n):
        self.Canceled = False
        self.n = n
        self.lock_obj = threading.Lock()

    def print_n(self):
        for i in range(1, self.n + 1):
            if self.Canceled:
                print("Stop")
                return
            print(i)

    def cancel(self):
        with self.lock_obj:
            self.Canceled = True


if __name__ == '__main__':
    p = print_nums(50000)
    t = threading.Thread(target=p.print_n)
    t.start()
    time.sleep(0.2)
    p.cancel()
    t.join()
    time.sleep(1)
    print("end of main")
