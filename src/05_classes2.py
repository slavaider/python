class Class:
    or1 = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f'create class {Class.__name__}')

    def display(self):
        return f'{self.x} - {self.y}'

    @classmethod
    def get_class(cls, x):
        return cls(x, 10)

    @staticmethod
    def get_class1(x):
        return Class(x, 10)


class Class1(Class):
    def __init__(self, z):
        Class.__init__(self, 1, 1)
        self.z = z
        print(f'create class {Class1.__name__}')

    def display(self):
        return f'{self.x} - {self.y} - {self.z}'


if __name__ == '__main__':
    # Creating class by init, class_method,staticmethod
    t = Class(1, 2)
    t1 = Class.get_class(1)
    t2 = Class.get_class1(1)
    print(t.display())
    print(t1.display())
    print(t2.display())
    # inheriting Class
    t3 = Class1(10)
    print(t3.display())
