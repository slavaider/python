from random import random

if __name__ == '__main__':

    M = 10
    N = 5
    a = []
    for i in range(N):
        b = []
        for j in range(M):
            b.append(int(random() * 11))
            print("%3d" % b[j], end='')
        a.append(b)
        print('   |', sum(b))

    for i in range(M):
        print(" --", end='')
    print()

    for i in range(M):
        s = 0
        for j in range(N):
            s += a[j][i]
        print("%3d" % s, end='')
    print()
