import random

if __name__ == '__main__':
    rand_list = [random.randint(0, 100) for _ in range(10)]
    print(rand_list)
    rand_list.reverse()
    # rand_list = rand_list[::-1]
    print(rand_list)
