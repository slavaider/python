if __name__ == '__main__':
    # Начало проги
    def window_create(width: int, height: int):
        print('#' * width)
        for i in range(height - 2):
            print('#' + ' ' * (width - 2) + '#')
        print('#' * width)


    window_create(30, 15)

    # string.split
    s = "SMITH a b c"
    print(s.split())

    dictionary = {
        'A': '1',
        'B':
            {
                'Q':
                    {
                        'd': '1',
                        'c': '3',
                        'g': '5'
                    }
            },
        'C': '88'
    }
    print(dictionary.get('A'))
