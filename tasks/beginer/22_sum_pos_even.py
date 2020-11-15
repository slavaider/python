import random

if __name__ == '__main__':
    list1 = [random.randint(-20, 20) for _ in range(10)]
    list2 = [i for i in list1 if i > 0]
    print(list1)
    print(sum(list2))
