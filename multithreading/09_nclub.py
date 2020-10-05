import threading
import time


class NightClub:
    def __init__(self):
        self.bouncer = threading.Semaphore(3)

    def open_club(self):
        for i in range(1, 51):
            t = threading.Thread(target=self.guest, args=[i])
            t.start()

    def guest(self, guest_id):
        print(f"\nguest {guest_id} is waiting")
        self.bouncer.acquire()
        print(f"\n{guest_id} is dancing ")
        time.sleep(1)
        print(f"\n{guest_id} is leaving ")
        self.bouncer.release()


if __name__ == "__main__":
    nc = NightClub()
    nc.open_club()
