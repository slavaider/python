import random

if __name__ == '__main__':
    rand_list = [random.randint(-5, 5) for _ in range(10)]
    print(rand_list)
    temp_list = [i for i in rand_list if i < 0]
    max_num = max(temp_list)
    max_pos = rand_list.index(max_num)
    print('Number', max_num, ', index:', max_pos)
