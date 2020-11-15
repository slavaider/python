import random

if __name__ == '__main__':
    list1 = [random.randint(0, 20) for _ in range(10)]
    max_num = 0
    for i in range(0, len(list1), 2):
        if list1[i] > list1[max_num]:
            max_num = i
    print(list1)
    print(max_num)
