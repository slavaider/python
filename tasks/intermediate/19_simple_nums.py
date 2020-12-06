import random

if __name__ == '__main__':
    rand_list = [random.randint(3, 10) for _ in range(10)]
    from math import sqrt

    count = 10
    for i in rand_list:
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                count -= 1
                break
    print(rand_list)
    print(count)
