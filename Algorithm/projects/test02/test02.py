import sys

sys.stdin = open('card.txt', 'r')

def shuffle(cards, div, x):
    left = cards[:div]
    right = cards[div:]
    cross = False
    result = []
    if div > x:
        for i in range(div):
            if i == div-x:
                cross = True
            if cross:
                result.append(right.pop(0))
                if left != []:
                    result.append(left.pop(0))
            else:
                result.append(left.pop(0))
        result += right
    else:
        for i in range(div):
            if i == x-div+1:
                cross = True
            if cross:
                result.append(left.pop(0))
                if right != []:
                    result.append(right.pop(0))
            else:
                result.append(right.pop(0))
        result += left
    return result



def get_x(n, k):
    global left, right, card_s, card_d, div, card, min_count

    if n == 5:

        cnt = 0
        sample = card.copy()
        for z in p:
            if cnt > min_count:
                break
            cnt += 1
            sample = shuffle(sample, div, z)
            if sample == card_s or sample == card_d:
                break
        else:
            cnt = 6
        if min_count > cnt:
            min_count = cnt
        return
    elif n > min_count:
        return
    else:
        for i in range(k):
            p[n] = x_list[i]
            get_x(n+1, k)



T = int(input())
for t in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    div = N//2
    card_s = sorted(card)
    card_d = card_s[::-1]
    x_list = list(range(1, N))
    p = [0] * 5
    min_count = 6
    if card == card_s or card == card_d:
        print("#{} 0".format(t))
        continue
    else:
        get_x(0, N-1)
    if min_count == 6:
        print("#{} -1".format(t))
    else:
        print("#{} {}".format(t, min_count))