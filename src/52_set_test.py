if __name__ == '__main__':
    s = {1, 2, 3}
    print(type(s))
    print(s)
    s.add(2)
    print()

    l1 = [1, 1, 1, 2, 3, 4, 5]
    s = set(l1)
    s.clear()
    # исходные данные
    print('исходные данные')
    print('s1 = ', s1 := {1, 2, 3, 4})
    print('s2 = ', s2 := {1, 2, 3, 4, 5})
    # подмножество
    print('s1 подмножество s2 :', s1.issubset(s2))
    # надмножество
    print('s2 надмножество s1 :', s2.issuperset(s1))
    # объединение s1+s2
    print('объединение s1 + s2')
    s3 = s1.union(s2)
    print(s3)
    # пересечение ||
    print('пересечение s1 || s2')
    s4 = s1.intersection(s2)
    print(s4)
    # &&
    print('симметрическая разница s1 && s2')
    s5 = s1.symmetric_difference(s2)
    print(s5)
    # update union without s3
    print('update is union s1,s2 without s3:result')
    s1.update(s2)
    print(s1)
    print()
    # remove,discard,pop
    s1.remove(1)
    s1.discard(2)
    print(s1.pop())
