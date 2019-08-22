import sys

sys.stdin = open('cabbage.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def search(x, y):
    global board
    global check

    board[x][y] = 2
    for z in range(4):
        x_ = x + dx[z]
        y_ = y + dy[z]
        if 0 <= x_ < M and 0 <= y_ < N:
            if board[x_][y_] == 1:
                search(x_, y_)
    return


T = int(input())
for t in range(1, T+1):
    M, N, K = map(int, input().split())
    board = [[0 for n in range(N)] for m in range(M)]
    cabbage = []
    for k in range(K):
        cabbage.append(list(map(int, input().split())))
    for c in cabbage:
        x, y = c
        board[x][y] = 1
    earthwarm = 0
    for cab in cabbage:
        x, y = cab
        if board[x][y] == 1:
            search(x, y)
            earthwarm += 1

    print(earthwarm)
