import random

if __name__ == '__main__':
    random_list = [random.randint(0, 99) for _ in range(10000)]
    counter = 0
    for i in random_list:
        if i % 2 == 0:
            counter += 1
    print((counter / 10000) * 100)
