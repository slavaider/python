import random
import threading
import time
from datetime import datetime


class HorseRace:
    def __init__(self):
        self.barrier = threading.Barrier(4)
        self.horses = ["1 horse", "2 horse", "3 horse", "4 horse"]
        self.finishers = []

    def lead(self):
        horse = self.horses.pop()
        time.sleep(random.randrange(1, 5))
        print(f"\n{horse} reached the barrier at {datetime.now()}")
        self.barrier.wait()
        time.sleep(random.randrange(1, 5))
        print(f"\n{horse} started at {datetime.now()}")
        time.sleep(random.randrange(1, 5))
        self.finishers.append(horse)
        print(f"\n{horse} finished at {datetime.now()}")
        self.barrier.wait()
        print(f"\n{horse} sleep")


if __name__ == "__main__":
    threads = []
    race = HorseRace()
    for i in range(len(race.horses)):
        threads.append(thread := threading.Thread(target=race.lead))
        thread.start()
    for i in range(len(threads)):
        threads[i].join()
    for i in range(len(race.finishers)):
        print(f"{i + 1} place take {race.finishers[i]}")
    print("end of main")
