import math

if __name__ == '__main__':
    n = 3  # rows
    m = 4  # cols
    matrix = []
    for i in range(n):
        temp = []
        for j in range(m):
            new = round(math.sin(n * (i + 1) + m * (j + 1)), 2)
            if new < 0:
                temp.append(0)
            else:
                temp.append(new)
            print(temp[j], end=' ')
        matrix.append(temp)
        print()
