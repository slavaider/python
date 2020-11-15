if __name__ == '__main__':
    n = 3  # rows
    m = 3  # cols
    matrix1 = [
        [234, 646, 862]
        , [148, 381, 57]
        , [530, 878, 951]
    ]

    matrix2 = [
        [1, 88, 23]
        , [234, 2, 5656]
        , [44, 342, 3]
    ]

    matrix3 = matrix2[0:]

    for i in range(n):
        for j in range(m):
            if matrix1[i][j] > matrix2[i][j]:
                matrix3[i][j] = matrix1[i][j]
            print(matrix3[i][j], end=' ')
        print()
