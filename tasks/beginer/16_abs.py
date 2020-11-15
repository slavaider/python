import random

if __name__ == '__main__':
    list1 = [random.randint(-15, 14) for _ in range(20)]
    max_num = max(list1)
    counter = 0
    for i in list1:
        if abs(i) > max_num:
            counter += 1
    print(list1)
    print(max_num)
    print(counter)
