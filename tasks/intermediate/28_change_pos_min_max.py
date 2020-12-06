import random

if __name__ == '__main__':
    rand_list = [random.randint(1, 1000) for _ in range(10)]
    pos_min = rand_list.index(min(rand_list))
    pos_max = rand_list.index(max(rand_list))
    print(rand_list)
    rand_list[pos_min], rand_list[pos_max] = rand_list[pos_max], rand_list[pos_min]
    print(rand_list)
