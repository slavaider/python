if __name__ == '__main__':
    # lists test
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    print(l1 + l2)
    l3 = [1, 2, 3]
    print(l1 + l2 + l3)
    l4 = ["12345", "lol1"]
    l4.sort(key=len)
    print(l4)
    l4.insert(0, "12")
    print(l4)
    print(l4.index('12'))
    l4.sort(reverse=True)
    print(l4)
    print(l4.count('0'))
    l5 = "123"
    print(l5.count('1'))
