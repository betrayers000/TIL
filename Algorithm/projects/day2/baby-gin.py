def check_run(cards):
    for i in range(7):
        if cards[i] != 0 and cards[i+1] != 0 and cards[i+2] != 0:
            cards[i] = cards[i] -1
            cards[i+1] = cards[i+1] - 1
            cards[i+2] = cards[i+2] - 1
            return cards, True
    return cards, False



def check_triple(cards):
    for i in range(10):
        if cards[i] >= 3:
            cards[i] = cards[i] -3
            return cards, True
    return cards, False



data = '054060'

cards = [0]*10

for i in data:
    cards[int(i)] = cards[int(i)] + 1


check_list = []
for j in range(2):
    cards, check = check_triple(cards)
    cards, check_2 = check_run(cards)
    check_list.append(check)
    check_list.append(check_2)

count = 0
for chek in check_list:
    if chek:
        count += 1
if count >= 2:
    print("baby-gin")
else :
    print("not baby-gin")
