import random

if __name__ == '__main__':
    list_items = [random.randint(-100, 100) for _ in range(10)]
    res = 0
    print(list_items)
    for i in list_items:
        for j in str(abs(i)):
            res += int(j)
    print(res)
