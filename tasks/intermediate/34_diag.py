if __name__ == '__main__':
    n = 10
    m = 10
    for i in range(n):
        print('#', end=' ')
        if i == 0 or i == n - 1:
            print('# ' * (m - 1), end=' ')
        else:
            for j in range(m - 2):
                if i - 1 == j or ((i - 1) == m - 3 - j):
                    print('+', end=' ')
                else:
                    print(' ', end=' ')
            print('#', end=' ')
        print()
