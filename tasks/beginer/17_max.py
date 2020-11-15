import random

if __name__ == '__main__':
    list1 = [random.randint(0, 20) for _ in range(10)]
    max_index = list1.index(max(list1))
    print(list1)
    print(list1[max_index], '- index:', max_index)
