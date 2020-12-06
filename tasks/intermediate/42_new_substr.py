if __name__ == '__main__':
    string = '11 22 33'
    print(string)
    string = string.replace(input('Prev substring: '), input('New substring: '))
    print(string)
