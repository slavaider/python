def greeting():
    print("Hello")


def print_name(name='Default'):
    print(name)


def is_palindrome(s):
    return s == s[::-1]


def cal(*args):
    return sum(args)


def players(**kwargs):
    for k, v in kwargs.items():
        print(f'player {k} is {v}')


greeting()
print_name("Lol")
print(is_palindrome('121'))
print(cal(1, 2, 3))
players(David=20, Roma=15)
