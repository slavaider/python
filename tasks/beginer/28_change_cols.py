import random

if __name__ == '__main__':
    rows = 3
    cols = 3
    max_value = 100
    matrix = [[random.randint(1, max_value) for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        print(matrix[i])

    c1 = int(input("Один столбец: ")) - 1
    c2 = int(input("Другой столбец: ")) - 1

    for i in range(rows):
        matrix[i][c1], matrix[i][c2] = matrix[i][c2], matrix[i][c1]
        print(matrix[i])
