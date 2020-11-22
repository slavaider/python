if __name__ == '__main__':
    letter = 'I dont like you!'
    upper = 0
    lower = 0
    for word in letter:
        if 'a' <= word <= 'z':
            lower += 1
        elif 'A' <= word <= 'Z':
            upper += 1
    print(f'{lower=},{upper=}')
