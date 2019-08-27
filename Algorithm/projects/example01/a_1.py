import sys

sys.stdin = open('input_a.txt', 'r')


def suffle(left, right, x, N):
    result = []
    cross = False
    if x < div:
        start = div-x
        for i in range(N):
            if cross:
                result.append(left.pop())
                result.append(right.pop())
            else:
                result.append(left.pop())





T = int(input())
for t in range(1, T + 1):
    N = int(input())
    card = list(map(int, input().split()))
    div = N // 2
    card_s = sorted(card)
    card_d = sorted(card)[::-1]
    left = card[:div]
    right = card[div:]
    print(card)

