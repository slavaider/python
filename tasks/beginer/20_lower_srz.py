import random

if __name__ == '__main__':
    list1 = [random.randint(0, 20) for _ in range(10)]
    srz = sum(list1) / len(list1)
    res = []
    for i in list1:
        if i < srz:
            res.append(i)
    print(list1)
    print(srz)
    print(res)
