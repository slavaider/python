if __name__ == '__main__':
    import math


    def circle(r):
        return math.pi * r ** 2


    def rectangle(a, b):
        return a * b


    def triangle(a, b, c):
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


    choice = input("Круг(к), прямоугольник(п) или треугольник(т): ")
    if choice == 'к':
        rad = float(input("Радиус: "))
        print("Площадь круга: %.2f" % circle(rad))
    elif choice == 'п':
        l = float(input("Длина: "))
        w = float(input("Ширина: "))
        print("Площадь прямоугольника: %.2f" % rectangle(l, w))
    elif choice == 'т':
        AB = float(input("Первая сторона: "))
        BC = float(input("Вторая сторона: "))
        CA = float(input("Третья сторона: "))
        print("Площадь треугольника: %.2f" % triangle(AB, BC, CA))
