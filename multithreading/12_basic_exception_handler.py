import threading
import time

thrown = False


def count():
    i = 0
    try:
        while True:
            if thrown:
                raise ZeroDivisionError
            i += 1
            print(i)
            time.sleep(1)
    except Exception as ex:
        print(repr(ex))


if __name__ == '__main__':
    t = threading.Thread(target=count)
    t.start()
    time.sleep(3)
    thrown = True
    for i in range(3):
        print(f'{i=}')
        time.sleep(1)
    print('Ended main')
