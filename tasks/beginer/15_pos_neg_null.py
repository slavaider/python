import random

if __name__ == '__main__':
    list1 = [random.randint(-5, 4) for _ in range(10)]
    pos = 0
    neg = 0
    zero = 0
    for i in list1:
        if i > 0:
            pos += 1
        elif i == 0:
            neg += 1
        else:
            zero += 1
    print(list1)
    print(f'{pos=}')
    print(f'{neg=}')
    print(f'{zero=}')
