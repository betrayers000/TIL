import sys

sys.stdin = open('baduk.txt', 'r')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

group_info = []


def f(x, y):
    global N, M, maxV
    s = []
    s.append([x, y])
    board[x][y] = -1
    temp = set()
    cnt = 0
    total = 0
    while s:
        i, j = s.pop()
        total += 1
        for k in range(4):
            ni, nj = i + dx[k], j + dy[k]
            if 0 <= ni < N and 0 <= nj < M and board[ni][nj] != 1:
                if board[ni][nj] == 2:
                    board[ni][nj] = -1
                    s.append([ni, nj])
                tn = len(temp)
                if board[ni][nj] == 0:
                    temp.add((ni, nj))
                    if tn != len(temp):
                        cnt += 1
    if cnt < 3:
        group_info.append((total, temp))


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
g = 3
idx = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            f(i, j)

# print(group_info)
# print(board)
n = len(group_info)
maxV = 0
for i in range(n):
    b, temp = group_info[i]
    cnt = b
    s_temp = set()
    for j in range(i + 1, n):
        nb, ntemp = group_info[j]
        q = temp | ntemp
        if len(q) <= 2 and len(s_temp | q) <= 2:
            cnt += nb
            s_temp = s_temp.union(temp | q)
    # print(s_temp, cnt)
    if cnt > maxV:
        maxV = cnt
    # print(maxV)
print(maxV)
