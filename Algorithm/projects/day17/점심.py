import sys

sys.stdin = open('lunch.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    s = []
    h = []
    num = 1
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                h.append([i, j])
            elif board[i][j] != 0:
                s.append([i, j, board[i][j], num])
                num += 1
    print(h, s)
    lh = len(h)
    for i in range(1, lh):
        a = i
        b = lh-i