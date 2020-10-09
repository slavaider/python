if __name__ == '__main__':
    table_cards = ["A_S", "J_H", "7_D", "8_D", "10_D"]
    hand_cards = ["J_D", "3_D"]
    deck = table_cards + hand_cards
    total_sum = 0
    while True:
        for i in range(len(deck)):
            if deck[i][2] == 'S':
                total_sum += 1
        if total_sum < 4:
            total_sum = 0
        else:
            print("Flush!")
            break
        for i in range(len(deck)):
            if deck[i][2] == 'H':
                total_sum += 1
        if total_sum < 4:
            total_sum = 0
        else:
            print("Flush!")
            break
        for i in range(len(deck)):
            if deck[i][2] == 'D':
                total_sum += 1
        if total_sum < 4:
            total_sum = 0
        else:
            print("Flush!")
            break
        for i in range(len(deck)):
            if deck[i][2] == 'C':
                total_sum += 1
        if total_sum < 4:
            total_sum = 0
            break
        else:
            print("Flush!")
            break
    if total_sum == 0:
        print("No Flush!")
