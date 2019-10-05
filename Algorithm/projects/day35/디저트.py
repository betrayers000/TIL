import sys

sys.stdin = open('dessert.txt', 'r')

dx = [1, 1, -1, -1]
dy = [-1, 1, -1, 1]


def f(x, y, c, s, n):
    global N, maxV, startI, startJ
    if c < 0:
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if nx == startI and ny == startJ and c < 3:
                if maxV < n+1:
                    maxV = n+1
                return
            if visited[nx][ny] == 0 and his[board[nx][ny]] == 0:
                visited[nx][ny] = 1
                his[board[nx][ny]] = 1
                if s != i:
                    f(nx, ny, c - 1, i, n + 1)
                else:
                    f(nx, ny, c, i, n + 1)
                visited[nx][ny] = 0
                his[board[nx][ny]] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    maxV = -1
    for i in range(N):
        for j in range(N):
            startI, startJ = i, j
            visited = [[0] * N for _ in range(N)]
            his = [0] * 101
            visited[i][j] = 1
            his[board[i][j]] = 1
            f(i, j, 4, -1, 0)
    print("#{} {}".format(t, maxV))
