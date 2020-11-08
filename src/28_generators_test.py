import itertools
from random import randint


def randoms(_min, _max, n):
    return [randint(_min, _max) for _ in range(n)]


def randoms1(min1, max1):
    while True:
        yield randint(min1, max1)


def read_file(file):
    while True:
        line = file.readline()
        if not line:
            break
        yield line


if __name__ == '__main__':
    for i in randoms(10, 30, 5):
        print(i)
    print()

    r1 = randoms1(10, 30)
    num = next(r1)
    print(f'{num=}')
    five = list(itertools.islice(r1, 5))
    print(f'{five=}')
    print()

    l1 = [1, 2, 3, 4]
    sq = (x ** 2 for x in l1)
    print(type(sq))
    for i in sq:
        print(i)
