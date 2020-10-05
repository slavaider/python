import threading
import time


def reference():
    print("start")
    lock_obj.acquire()
    print("acquired")
    reference()


def f1():
    print("run t1")
    print("t1 join t2")
    time.sleep(2)
    t2.join()
    print("sleep t1")
    time.sleep(5)
    print("end of t1")


def f2():
    print("run t2")
    print("t2 join t1")
    time.sleep(2)
    t1.join()
    print("sleep t2")
    time.sleep(5)
    print("end of t2")


a = 5
b = 5


def t1_calc():
    global a
    global b
    print("t1 req a")
    a_lock.acquire()
    time.sleep(5)
    print("t1 req b")
    b_lock.acquire()
    time.sleep(5)
    a += 5
    b += 5
    print("t1 release both lock")
    a_lock.release()
    b_lock.release()


def t2_calc():
    global a
    global b
    print("t2 req b")
    b_lock.acquire()
    time.sleep(5)
    print("t2 req a")
    a_lock.acquire()
    time.sleep(5)
    a += 5
    b += 5
    print("t1 release both lock")
    a_lock.release()
    b_lock.release()


if __name__ == "__main__":
    lock_obj = threading.Lock()

    # try to acquire already locked object ->deadlock
    # print("acquire 1st time")
    # lock_obj.acquire()
    # print("acquire 2nd time")
    # lock_obj.acquire()
    # print("release")
    # lock_obj.release()

    # recurse acquire obj
    # reference()
    # print("end ref")

    # t1.join(t2) t2.join(t1)
    # t1 = threading.Thread(target=f1)
    # t2 = threading.Thread(target=f2)
    # t1.start()
    # t2.start()

    # 2 locks
    # a_lock = threading.Lock()
    # b_lock = threading.Lock()
    # t1 = threading.Thread(target=t1_calc)
    # t2 = threading.Thread(target=t2_calc)
    # t1.start()
    # t2.start()
