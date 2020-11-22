for i in range(0, 55296):
    print("%4d-%s" % (i, chr(i)), end=' ')
    if (i - 1) % 15 == 0:
        print()
