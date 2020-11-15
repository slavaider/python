if __name__ == '__main__':
    list1 = [10, -8, 12, 3, -14, -3, -14, -15, 9, -7, 6, -3, -1, -11, -2, -13, 1, -7, 8, -10]
    list2 = [abs(i) for i in list1]
    min_num = min(list2)
    res = []
    for i in range(len(list2)):
        if list2[i] == min_num:
            res.append(i+1)
    print(min_num, res)
