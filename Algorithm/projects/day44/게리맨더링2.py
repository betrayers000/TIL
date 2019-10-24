import sys

sys.stdin = open('gary.txt')

dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]


def visit_px(i, j, ni, nj, c):
    global N
    temp = 0
    if 0 <= i < N and 0 <= j < N and 0 <= ni < N and 0 <= nj < N:
        while visited[ni][nj] == 0:
            visited[ni][nj] = 1
            temp += board[ni][nj]
            if c == 0:
                visited[ni-1][nj] = 1
                temp+= board[ni-1][nj]
            ni -= 1
            nj += 1
            try:
                visited[ni][nj]
            except:
                break
    return temp

def f(i, j, ni, nj, ui, uj, di, dj):
    global N
    t1, t2, t3, t4 = 0, 0, 0, 0
    for x in range(ni):
        for y in range(j+1):
            if visited[x][y] == 0:
                t1 += board[x][y]
                visited[x][y] = 2
    for x in range(ui+1):
        for y in range(j+1, N):
            if visited[x][y] == 0:
                t2 += board[x][y]
                visited[x][y] = 3
    for x in range(ni, N):
        for y in range(dj):
            if visited[x][y] == 0:
                t3 += board[x][y]
                visited[x][y] = 4
    for x in range(ui+1, N):
        for y in range(dj, N):
            if visited[x][y] == 0:
                t4 += board[x][y]
                visited[x][y] = 5
    return [t1, t2, t3, t4]

def copy_list(temp):
    global N
    res = []
    for i in range(N):
        res.append(temp[i].copy())
    return res



N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
minV = 9999999999
for i in range(N):
    for j in range(N):
        nj = j - 1
        ni = i + 1
        while 0 <= ni < N and 0 <= nj < N:
            total = board[i][j]
            visited = [[0] * N for _ in range(N)]
            visited[i][j] = 1
            total += visit_px(i, j, ni, nj, 1)
            lk = N - j - 1
            for k in range(1, N - j):
                di, dj = ni + k, nj + k
                ui, uj = i + k, j + k
                if 0 <= di < N and 0 <= dj < N and 0 <= ui < N and 0 <= uj < N:
                    total += board[ui][uj]
                    visited[ui][uj] = 1
                else:
                    break
                ans = visit_px(ui, uj, di, dj, 0)
                total += ans
                temp = copy_list(visited)
                res_list = f(i, j, ni, nj, ui, uj, di, dj)
                res_list.append(total)
                res = max(res_list)-min(res_list)
                # print(visited, res)
                # print(visited, total)
                if minV > res:
                    minV = res
                visited = temp
            ni += 1
            nj -= 1
print(minV)
