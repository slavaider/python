import threading
import time


class StopEvent(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(StopEvent, self).__init__(*args, **kwargs)
        self.CanceledEvent = threading.Event()

    def stop(self):
        self.CanceledEvent.set()

    def canceled(self):
        return self.CanceledEvent.is_set()


class print_nums(StopEvent):
    def __init__(self, n, name="Test_Thread"):
        super().__init__(name=name)
        self.n = n

    def run(self):
        print(f"\n{self.getName()} run")
        self.work()
        print(f"\n{self.getName()} end")

    def work(self):
        for i in range(1, self.n + 1):
            if super().canceled():
                print("\nStop")
                return self
            print(i)


if __name__ == '__main__':
    p = print_nums(50000)
    p.start()
    time.sleep(5)
    p.stop()
    p.join()
    time.sleep(1)
    print("end of main")
