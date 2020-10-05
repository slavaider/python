if __name__ == '__main__':
    word = 'bottles'
    for i in range(10, 0, -1):
        print(i, word, 'of beer on the wall')
        print(i, word, 'of beer')
        print('take 1 down')
        print('pass it around')
        if i == 1:
            print('No more bottles on wall')
        else:
            new_num = i - 1
            if new_num == 1:
                word = 'bottle'
            print(new_num, word, 'of beer on the wall')
        print()
