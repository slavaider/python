if __name__ == '__main__':
    a = [0] * 8
    for i in range(2, 100):
        for j in range(2, 10):
            if i % j == 0:
                a[j - 2] += 1
    i = 0
    for i in range(len(a)):
        print(i + 2, ' - ', a[i])
