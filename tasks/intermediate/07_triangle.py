def triangle(a: float, b: float, c: float):
    if a + b <= c or b + c <= a or a + c <= b:
        print('Треугольник не существует')
    elif a != b and a != c and b != c:
        print('Это разносторонний треугольник.')
    elif a == b and b == c:
        print('Это равносторонний треугольник.')
    else:
        print('Это равнобедренный треугольник.')


if __name__ == '__main__':
    triangle(5, 5, 5)
