if __name__ == '__main__':
    a = 5
    print("%d = %s" % (a, bin(a)))
    b = 6
    print("%d = %s" % (b, bin(b)))

    print("%d & %d = %d (%s)" % (a, b, a & b, bin(a & b)))
    print("%d | %d = %d (%s)" % (a, b, a | b, bin(a | b)))
    print("%d ^ %d = %d (%s)" % (a, b, a ^ b, bin(a ^ b)))
    print("%d << 2 = %d (%s)" % (b, b << 2, bin(b << 2)))
    print("%d >> 2 = %d (%s)" % (b, b >> 2, bin(b >> 2)))
