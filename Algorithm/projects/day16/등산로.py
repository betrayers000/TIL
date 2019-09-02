import sys

sys.stdin = open('hiking.txt', 'r')


def dfs(point, total):
    global max_road, digging, K
    x, y = point
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(4):
        x_ = x + dx[i]
        y_ = y + dy[i]
        if 0 <= x_ < N and 0 <= y_ < N:
            if board[x][y] > board[x_][y_] and visited[x_][y_] == 0:
                visited[x][y] = 1
                dfs([x_, y_], total + 1)
                visited[x][y] = 0
            else:
                if digging and board[x_][y_] < board[x][y] + K and visited[x_][y_] == 0:
                    digging = False
                    visited[x][y] = 1
                    org = board[x_][y_]
                    board[x_][y_] = board[x][y] - 1
                    dfs([x_, y_], total + 1)
                    visited[x][y] = 0
                    board[x_][y_] = org
                    digging = True
    if max_road < total:
        max_road = total


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_ = 0
    for i in range(N):
        for j in range(N):
            if max_ < board[i][j]:
                max_ = board[i][j]
    visited = [[0] * N for _ in range(N)]
    max_road = 0
    digging = True
    check = True
    for i in range(N):
        for j in range(N):
            if board[i][j] == max_:
                dfs([i, j], 1)
    print(max_road)
