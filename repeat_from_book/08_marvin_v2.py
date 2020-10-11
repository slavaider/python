if __name__ == '__main__':
    paranoid_android = 'Marvin, the Paranoid Android'
    letters = list(paranoid_android)
    print('1 for')
    for char in letters[:6]:
        print('\t', char)
    print('2 for')
    for char in letters[-7:]:
        print('\t'*2, char)
    print('3 for')
    for char in letters[12:20]:
        print('\t'*3, char)
