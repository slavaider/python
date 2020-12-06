import random

if __name__ == '__main__':
    rand_list = [random.randint(-5, 5) for _ in range(10)]
    pos = []
    neg = []
    for i in rand_list:
        if i >= 0:
            pos.append(i)
        elif i < 0:
            neg.append(i)
    print(rand_list)
    print(pos)
    print(neg)
