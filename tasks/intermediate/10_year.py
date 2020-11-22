if __name__ == '__main__':
    y = int(input('year = '))
    if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
        print("Обычный")
    else:
        print("Високосный")
