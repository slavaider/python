def count_vowels(s):
    summa = 0
    lol = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}
    for letter in s:
        if lol.get(letter) and lol[letter]:
            summa += 1
    return summa


# print(count_vowels("abcd"))  # 1


def is_full_house(lst):
    # temp = 0
    # temp_letter = ""
    # temp1 = 0
    # temp1_letter = ""
    # for i in lst:
    #     if temp_letter == "":
    #         temp_letter = i
    #         temp += 1
    #     elif temp_letter == i:
    #         temp += 1
    #     elif temp1_letter == "":
    #         temp1_letter = i
    #         temp1 += 1
    #     elif temp1_letter == i:
    #         temp1 += 1
    # return True if ((temp == 3 and temp1 == 2 or temp == 2 and temp1 == 3) and temp + temp1 == 5) else False
    return all([lst.count(i) >= 2 for i in lst])


print(is_full_house(["A", "J", "J", "A", "A"]))


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

#
# print(check_sequence([1, 2, 3]))  # 1
# print(check_sequence([3, 2, 1]))  # -1
# print(check_sequence([1, 2, 1]))  # 0
# print(check_sequence([1, 1, 2]))  # 0
