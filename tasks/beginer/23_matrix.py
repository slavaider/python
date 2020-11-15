if __name__ == '__main__':
    m = 7  # cols
    n = 5  # rows
    # matrix = [[random.randint(0, 999) for _ in range(m)] for _ in range(n)]
    matrix = [
        [234, 646, 862, 863, 324, 718, 465]
        , [148, 381, 57, 577, 982, 728, 112]
        , [530, 878, 951, 93, 410, 252, 332]
        , [161, 275, 180, 235, 19, 70, 881]
        , [321, 226, 500, 871, 318, 685, 958]
    ]
    counter = 0
    for i in range(n):
        for j in range(m):
            if 10 < matrix[i][j] < 99:
                counter += 1
    print(counter)
