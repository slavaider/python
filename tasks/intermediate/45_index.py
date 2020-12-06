if __name__ == '__main__':
    s = input()
    if 'a' <= s[0].lower() <= 'z' or s[0] == '_':
        for i in range(1, len(s)):
            if not ('a' <= s[i].lower() <= 'z'
                    or '0' <= s[i].lower() <= '9'
                    or s[i].lower() == '_'):
                print('No')
                quit()
        print('Yes')
    else:
        print('No')
