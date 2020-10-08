class st:
    or1 = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f'create class {st.__name__}')

    def display(self):
        return f'{self.x} - {self.y}'

    @classmethod
    def get_class(cls, x):
        return cls(x, 10)

    @staticmethod
    def get_class1(x):
        return st(x, 10)


class st1(st):
    def __init__(self, z):
        st.__init__(self, 1, 1)
        self.z = z
        print(f'create class {st1.__name__}')

    def display(self):
        return f'{self.x} - {self.y} - {self.z}'


if __name__ == '__main__':
    t = st(1, 2)
    t1 = st.get_class(1)
    t2 = st.get_class1(1)
    print(t.display())
    print(t1.display())
    print(t2.display())
    t3 = st1(10)
    print(t3.display())
    # string.split
    s = "SMITH a b c"
    print(s.split())
