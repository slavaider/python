import random

if __name__ == '__main__':
    rand_list = [random.randint(0, 100) for _ in range(10)]
    max_sum = 0
    max_num = 0
    for i in rand_list:
        temp = 0
        for num in str(i):
            temp += int(num)
        if temp > max_sum:
            max_sum = temp
            max_num = i
    print(rand_list)
    print('Число', max_num, 'имеет максимальную сумму цифр:', max_sum)
