def square(number):
    return number * number


def is_a(age): return age > 18


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = list(map(square, list1))
    print(list2)
    l1 = [10, 12, 19, 20]
    l2 = list(filter(lambda age: age > 18, l1))
    print(l2)
    l2 = [i for i in l1 if is_a(i)]
    print(l2)
