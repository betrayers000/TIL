import sys

sys.stdin = open('tr.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(i, j, c):
    global maxV
    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        if 0 <= nx < R and 0 <= ny < C:
            n = ord(board[nx][ny]) - 65
            if visited[n] == 0:
                visited[n] = 1
                dfs(nx, ny, c+1)
                visited[n] = 0
    if maxV < c:
        maxV = c

T = int(input())
for t in range(1, T + 1):
    R, C = map(int, input().split())
    board = [list(input()) for _ in range(R)]
    maxV = 0
    visited = [0] * 26
    visited[ord(board[0][0])-65] = 1
    dfs(0, 0, 1)
    print("#{} {}".format(t, maxV))
