def is_palindrome(s):
    return s == s[::-1]


if __name__ == '__main__':
    str_number = input("Введите число на проверку на палиндром = ")
    number = int(str_number)
    copy = 0
    copy1 = number
    while number // 10 != 0:
        copy = copy * 10 + (number % 10)
        number //= 10
    copy = copy * 10 + number
    if copy == copy1:
        print("Palindrome")
    else:
        print("Not Palindrome")
    print()

    # alternate with str
    if is_palindrome(str_number):
        print("Palindrome")
    else:
        print("Not Palindrome")
    # alternate with int
    # number = int(input("Введите число на проверку на палиндром = "))
    # import sys
    # number = sys.argv[1]
    # res = [int(x) for x in str(number)]
    # copy = res.copy()
    # copy.reverse()
    # if res == copy:
    #     print("Palindrome")
    # else:
    #     print("Not Palindrome")
