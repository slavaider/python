import random

if __name__ == '__main__':
    n = 3
    list1 = [random.randint(0, 99) for _ in range(3)]
    list2 = [int(input('Введите число = ')) for _ in range(3)]
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i] + list2[i])
    print(list1)
    print(list2)
    print(list3)
