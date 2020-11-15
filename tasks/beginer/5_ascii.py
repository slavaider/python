if __name__ == '__main__':
    n = int(input())
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    if a <= n <= z or A <= n <= Z:
        print('Это буква', chr(n))
    else:
        print('Это не буква, а символ', chr(n))
