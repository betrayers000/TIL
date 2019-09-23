import sys

sys.stdin = open('min.txt', 'r')

q = []


def f(i, j):
    global d, board
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if 0 <= ni < N and 0 <= nj < N:
            s = 0
            if board[ni][nj] > board[i][j]:
                s = board[ni][nj] - board[i][j]
            d[ni][nj] = min(d[ni][nj], d[i][j] + s + 1)
            q.append([ni, nj])


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    d = [[1000 * N * N] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    d[0][0] = 0
    q.append([0, 0])
    while 1:
        minV = 1000 * N * N
        idx = 0
        for k in range(len(q)):
            i, j = q[k]
            if d[i][j] != 1000 * N * N and visited[i][j] == 0:
                if minV > d[i][j]:
                    minV = d[i][j]
                    idx = k
        if q == []:
            break
        mi, mj = q.pop(idx)
        f(mi, mj)
        visited[mi][mj] = 1
        if visited[N - 1][N - 1] == 1:
            break
    print("#{} {}".format(t, d[N - 1][N - 1]))
