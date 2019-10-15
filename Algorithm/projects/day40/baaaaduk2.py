import sys

sys.stdin = open('baduk.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def get_black(p):
    temp = []
    for i in range(2):
        x, y = empty[p[i]]
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 2:
                    temp.append([nx, ny])
    return temp


def dfs(black):
    global N, M
    visited = [[0] * M for _ in range(N)]
    total = 0
    for k in range(len(black)):
        x_, y_ = black[k]
        s = []
        s.append(black[k])
        if visited[x_][y_] == 1:
            continue
        visited[x_][y_] = 1
        check = True
        cnt = 0
        while s:
            x, y = s.pop()
            cnt += 1
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                    if board[nx][ny] == 2:
                        visited[nx][ny] = 1
                        s.append([nx, ny])
                    elif board[nx][ny] == 0:
                        check = False
        if check:
            total += cnt
    return total


def f(n, k, m, z):
    global maxV
    if n == m:
        black = get_black(p.copy())
        # print(p, black)
        if len(black) < 2:
            return
        res = dfs(black)
        if maxV < res:
            maxV = res
        return
    else:
        for i in range(z, k):
            if used[i] == 0:
                p[n] = i
                board[empty[i][0]][empty[i][1]] = 1
                used[i] = 1
                f(n + 1, k, m, i)
                used[i] = 0
                board[empty[i][0]][empty[i][1]] = 0


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
empty = []
maxV = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            empty.append([i, j])
n = len(empty)
p = [0] * 2
used = [0] * n
f(0, n, 2, 0)
print(maxV)
