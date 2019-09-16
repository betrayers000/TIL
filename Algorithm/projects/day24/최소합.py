import sys

sys.stdin = open('minsum.txt', 'r')


def f(point, s):
    global N, minV
    dx = [0, 1]
    dy = [1, 0]
    x, y = point
    if x == N-1 and y == N-1:
        if s < minV:
            minV = s
        return
    if s > minV:
        return
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            f([nx, ny], s + board[nx][ny])


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    minV = sum(board[0])
    for i in range(N):
        minV += board[i][N - 1]
    f([0,0],board[0][0])
    print(minV)
