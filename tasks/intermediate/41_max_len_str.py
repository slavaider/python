if __name__ == '__main__':
    letter = 'Hello world and me!!!'
    letter1 = 'Hello world and me!!!'
    letter2 = 'Hello'
    list_items = [letter, letter1, letter2]
    pos_max = [i for i in range(len(list_items)) if list_items[i] == max(list_items)]
    print(pos_max)
