import random

if __name__ == '__main__':
    rand_list = [random.randint(0, 100) for _ in range(10)]
    evens_index = []
    print(rand_list)
    for i in range(len(rand_list)):
        if rand_list[i] % 2 == 0:
            evens_index.append(i)
    print(evens_index)
