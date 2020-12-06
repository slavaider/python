import random

if __name__ == '__main__':
    rand_list = [random.randint(1, 5) for _ in range(10)]
    unique = []
    print(rand_list)
    for i in rand_list:
        if rand_list.count(i) == 1:
            unique.append(i)
    print(sorted(unique))
