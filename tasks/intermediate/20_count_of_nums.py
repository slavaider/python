import random

if __name__ == '__main__':
    rand_list = [random.randint(0, 1000) for _ in range(10)]
    num = 0
    counter = 0
    for i in rand_list:
        for j in str(i):
            if int(j) == num:
                counter += 1
    print(rand_list)
    print(f'NUmber: {num} - {counter}')
