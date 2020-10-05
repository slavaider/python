if __name__ == '__main__':
    phrase = "Don't panic!"
    plist = list(phrase)
    print(phrase)
    print(plist)
    print('Begin')

    new_phrase = ''.join(plist[1:3])
    new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])
    # plist = plist[1:8] alt
    # plist.remove("'")
    # plist.insert(2, plist.pop(3))
    # plist.insert(4, plist.pop(5))
    #
    # new_phrase = ''.join(plist)
    # print(plist)
    print(new_phrase)
