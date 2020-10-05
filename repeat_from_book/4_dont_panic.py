if __name__ == '__main__':
    phrase = "Don't panic!"
    plist = list(phrase)
    print(phrase)
    print(plist)

    temp = []
    temp.extend(plist[1:3])
    temp.append(plist.pop(5))
    temp.insert(3, plist.pop(4))
    temp.append(plist.pop(5))
    temp.append(plist.pop(4))
    plist = temp

    new_phrase = ''.join(plist)
    print(plist)
    print(new_phrase)
