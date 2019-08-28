import sys

sys.stdin = open('input_a.txt', 'r')


def suffle(left, right, x, div):





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

