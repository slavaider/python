import concurrent.futures
import threading
import time


class BankAcc:
    def __init__(self):
        self.balance = 100  # shared
        self.lock_obj = threading.Lock()

    def update(self, transaction, amount):
        print(f"{transaction} start")
        with self.lock_obj:
            tmp_balance = self.balance
            tmp_balance += amount
            time.sleep(1)
            self.balance = tmp_balance
        print(f"{transaction} end")

    def update_race(self, transaction, amount):
        print(f"{transaction} start")
        tmp_balance = self.balance
        tmp_balance += amount
        time.sleep(1)
        self.balance = tmp_balance
        print(f"{transaction} end")


if __name__ == "__main__":
    # lock_obj = threading.Lock()
    # print(lock_obj.locked())
    # lock_obj.acquire()
    # print(lock_obj.locked())
    # lock_obj.release()
    # print(lock_obj.locked())

    acc = BankAcc()
    print(f"main start")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(acc.update, ("refill", "withdraw"), (100, -200))
    print(f"{acc.balance}")
    print(f"main end")
