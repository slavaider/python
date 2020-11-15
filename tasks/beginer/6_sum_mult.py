if __name__ == '__main__':

    # 1 path
    # x = list(input('x='))
    # x = [int(i) for i in x]
    # print(sum(x))
    # res = x[0]
    # for i in range(len(x) - 1):
    #     res *= x[i + 1]
    # print(res)

    # 2 path
    n = int(input('x='))
    s = 0
    m = 1
    while n > 0:
        s += n % 10
        m *= n % 10
        n = n // 10
    print("Сумма:", s)
    print("Произведение:", m)
