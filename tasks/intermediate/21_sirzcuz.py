import random

if __name__ == '__main__':
    # Если число четное следует разделить его на 2.
    # Если нечетное, то умножить его на 3, прибавить 1 и разделить на 2.
    rand_list = [random.randint(0, 1000) for _ in range(10)]
    for i in rand_list:
        print('-> ', i, end=' ')
        while i != 1:
            if i % 2 == 0:
                i //= 2
            elif i % 2 == 1:
                i = (i * 3 + 1) // 2
            print(i, end=' ')
        print()