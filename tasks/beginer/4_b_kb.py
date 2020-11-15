if __name__ == '__main__':
    x = input('x=')
    format = x[-1]
    if format == 'b':
        print(int(x[0:-1]) * 1024)
    elif format == 'k':
        print(int(x[0:-1]) // 1024)
