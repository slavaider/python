if __name__ == '__main__':
    string = 'abc cde def'
    s_new = ''
    for i in string:
        if i not in s_new and i != ' ':
            s_new += i
    print(s_new)
