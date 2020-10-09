if __name__ == '__main__':
    l1 = [1, 2, 3, 4, 5, 6]  # %2==1
    l2 = [2, 4, 6, 7, 3, 12, 4]  # %2==0
    l3 = sum([i + j for i in l1 if i % 2 == 0 for j in l2 if j % 2 == 1])
    print(l3)
