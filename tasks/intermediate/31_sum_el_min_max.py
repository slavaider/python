import random

if __name__ == '__main__':
    rand_list = [random.randint(-100, 100) for _ in range(10)]
    print(rand_list)
    pos_min = rand_list.index(min(rand_list))
    pos_max = rand_list.index(max(rand_list))
    res_sum = 0
    print('pos_min ', pos_min, ' pos_max ', pos_max)
    if pos_max > pos_min:
        for i in range(pos_min + 1, pos_max):
            res_sum += rand_list[i]
    elif pos_min > pos_max:
        for i in range(pos_max + 1, pos_min):
            res_sum += rand_list[i]
    print(res_sum)
