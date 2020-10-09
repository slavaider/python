def count_vowels(s):
    total_sum = 0
    dict = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}
    for letter in s:
        if dict.get(letter) and dict[letter]:
            total_sum += 1
    return total_sum


def is_full_house(lst):
    return all([lst.count(i) >= 2 for i in lst])


def check_sequence(lst):
    mode = 0
    flag = True
    for i in range(len(lst) - 1):
        if flag and lst[i] < lst[i + 1]:
            mode = 1
        elif (lst[i] == lst[i + 1]) or mode == 1 and lst[i] > lst[i + 1]:
            mode = 0
            break
        elif lst[i] > lst[i + 1]:
            mode = -1
            flag = False
    return mode


if __name__ == '__main__':
    # 1
    print(count_vowels("abcd"))
    # 2
    print(is_full_house(["A", "J", "J", "A", "A"]))
    # 3
    print(check_sequence([1, 2, 3]))  # 1
    print(check_sequence([3, 2, 1]))  # -1
    print(check_sequence([1, 2, 1]))  # 0
    print(check_sequence([1, 1, 2]))  # 0
