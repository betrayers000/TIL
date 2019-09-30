import sys

sys.stdin = open('square.txt', 'r')
sys.setrecursionlimit(10**6)




# def f(i, j, c, z):
#     global maxV, N
#     if memo[i][j] != 0:
#         if maxV <= memo[i][j] + c:
#             maxV = memo[i][j] + c
#             res.append(room[z[0]][z[1]])
#             memo[z[0]][z[1]] = memo[i][j] + c
#             return
#     else:
#         for k in range(4):
#             ni, nj = i + dx[k], j + dy[k]
#             if 0 <= ni < N and 0 <= nj < N and room[i][j] + 1 == room[ni][nj]:
#                 if memo[i][j] == 0:
#                     f(ni, nj, c + 1, z)
#                     break
#     if maxV <= c and c != 0:
#         maxV = c
#         res.append(room[z[0]][z[1]])
#         memo[z[0]][z[0]] = c

def dfs(i, j):
    global maxV, minV
    s = []
    s.append([i, j])
    cnt = 0
    while s:
        x, y = s.pop()
        if memo[x][y] != 0:
            cnt += memo[x][y]
            break
        for k in range(4):
            ni, nj = x + dx[k], y + dy[k]
            if 0 <= ni < N and 0 <= nj < N and room[x][y] + 1 == room[ni][nj]:
                s.append([ni, nj])
                cnt += 1
                break
    memo[i][j] = cnt
    if maxV <= cnt and cnt != 0:
        if maxV < cnt:
            minV = room[i][j]
        else:
            if minV > room[i][j]:
                minV = room[i][j]
        maxV = cnt


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    maxV = 1
    minV = N*N
    memo = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dfs(i, j)
    print("#{} {} {}".format(t, minV, maxV+1))
