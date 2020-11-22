if __name__ == '__main__':
    with open('../../files/test_file.txt', mode='w+') as file:
        line = input('Введите строку = ')
        while line != '':
            file.write(line + '\n')
            line = input('Введите строку = ')
    with open('../../files/test_file.txt', mode='r') as file:
        letters = file.read()
        print(letters)
