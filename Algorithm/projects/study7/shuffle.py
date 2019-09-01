import sys
import timeit

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


def bfs(card, div, N):
    q = [0] * 25
    front, rear = -1, -1
    rear += 1
    q[rear] = [card]
    while front < 5:
        front += 1
        now_x = q[front]
        temp = []
        for now in now_x:
            for i in range(1, N):
                next_card = shuffle(now, div, i)
                if next_card == card_s or next_card == card_d:
                    return front+1
                else:
                    temp.append(next_card)
        rear += 1
        q[rear] = temp
    return -1


time_start = timeit.default_timer()
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
        print(f"#{t} 0")
        continue
    else:
        result = bfs(card, div, N)
        print(f"#{t} {result}")
end = timeit.default_timer()
print(end - time_start)
    # if min_count == 6:
    #     print("#{} -1".format(t))
    # else:
    #     print("#{} {}".format(t, min_count))