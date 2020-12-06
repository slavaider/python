if __name__ == '__main__':
    # 1+2+...+n = n(n+1)/2,
    n = 141
    res_sum = 0
    for i in range(1, n + 1):
        res_sum += i
    if res_sum == (n * (n + 1)) // 2:
        print('Верно')
    else:
        print('Неверно')
