number = int(input("Введите число на проверку на палиндром = "))
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
# alt
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
