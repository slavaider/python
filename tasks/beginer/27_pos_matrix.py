import random

if __name__ == '__main__':
    rows = 3
    cols = 3
    max_value = 100
    matrix = [[random.randint(-100, max_value) for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=' ')
        print()

    for i in range(rows):
        if matrix[i][i] > 0:
            print('Row: %d, col: %d' % (i + 1, i + 1))
