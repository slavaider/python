import math


def triangle(a: float, b: float, c: float):
    # Периметр треугольника: P = a + b + c
    # Площадь треугольника: S = √(p(p-a)(p-b)(p-c)), где p = P/2
    p = (a + b + c) / 2
    return {'perimeter': a + b + c, 'square': math.sqrt(p * (p - a) * (p - b) * (p - c))}


def rectangle(a: float, b: float):
    # Периметр прямоугольника: P = 2(a + b)
    # Площадь прямоугольника: S = ab
    return {'perimeter': 2 * (a + b), 'square': a * b}


def circle(r: float):
    # Периметр круга: P = 2πr
    # Площадь круга: S = πr^2
    return {'perimeter': 2 * math.pi * r, 'square': math.pi * (r ** 2)}


if __name__ == '__main__':
    # треугольника по данным трем сторонам,
    # прямоугольника по данным ширине и высоте,
    # круга по заданному радиусу.
    mode = input('mode[triangle:t,rectangle:r,circle:c] = ')
    if mode == 'r':
        a = float(input('a = '))
        b = float(input('b = '))
        result = rectangle(a, b)
        print('perimeter = ', result['perimeter'], 'square = ', result['square'])
    elif mode == 't':
        a = float(input('a = '))
        b = float(input('b = '))
        c = float(input('c = '))
        result = triangle(a, b, c)
        print('perimeter = ', result['perimeter'], 'square = ', result['square'])
    elif mode == 'c':
        r = float(input('r = '))
        result = circle(r)
        print('perimeter = ', result['perimeter'], 'square = ', result['square'])
