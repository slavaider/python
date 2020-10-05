# Начало проги
def window_create(width: int, height: int):
    print('#' * width)
    for i in range(height - 2):
        print('#' + ' ' * (width - 2) + '#')
    print('#' * width)


window_create(30, 15)
