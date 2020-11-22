import random

if __name__ == '__main__':
    rows = 3
    cols = 3
    max_value = 100
    matrix = [[random.randint(1, max_value) for _ in range(cols)] for _ in range(rows)]
    min_value = max_value + 1
    for i in range(rows):
        min_i = min(matrix[i])
        if min_i < min_value:
            min_value = min_i
    print(f'{min_value=}')

    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=' ')
        print()

    for i in range(rows):
        for j in range(cols):
            if min_value == matrix[i][j]:
                print('Row: %d, col: %d' % (i + 1, j + 1))
