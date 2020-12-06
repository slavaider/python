import random

if __name__ == '__main__':
    rand_list = [random.randint(-5, 5) for _ in range(10)]
    print(rand_list)
    first = min(rand_list)
    rand_list.remove(first)
    second = min(rand_list)
    print(f'{first=}, {second=}')
