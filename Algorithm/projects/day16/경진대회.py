import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    players = [int(input()) for _ in range(N)]
    players.sort()
    last = players[-1]
    cnt = 0
    for player in players:
        if last + 1 <= player + N:
            cnt += 1
    print("Case #{}".format(t))
    print(cnt)



