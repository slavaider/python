if __name__ == '__main__':

    print('Function in function')


    def apply(func: object, value: object):
        return print(func(value))


    apply(repr, 23)
    apply(id, 23)
    apply(len, '123')
    apply(print, 123)

    print('Arguments')


    def func1(*args):
        if args:
            for item in args:
                print(item)
            print()


    def func2(**kwargs):
        if kwargs:
            for k, v in kwargs.items():
                print(k, '->', v)
            print()


    def func3(*args, **kwargs):
        if args:
            for item in args:
                print(item)
            print()
        if kwargs:
            for k, v in kwargs.items():
                print(k, '->', v)
            print()


    lst = [1, 2, 3, 4]
    dictionary = {'a': 1, 'b': 2, 'c': 3}
    func1(lst)
    func2(**dictionary)
    func3(lst, **dictionary)
