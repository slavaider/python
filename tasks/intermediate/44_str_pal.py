if __name__ == '__main__':
    string = '123    321'
    string = string.replace(' ', '')
    if string == string[::-1]:
        print('Palindrome')
    else:
        print('Not Palindrome')
