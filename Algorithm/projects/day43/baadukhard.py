import sys

sys.stdin = open('baduk.txt', 'r')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def f(x, y):
    global N, M, maxV
    s = []
    temp = [[x, y]]
    s.append([x, y])
    total = 0
    while s:
        i, j = s.pop()
        for k in range(4):
            ni, nj = i + dx[k], j + dy[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                if board[ni][nj] == 2:
                    visited[ni][nj] = 1
                    s.append([ni, nj])
                    temp.append([ni, nj])
                # elif board[ni][nj] == 0 and total < 2:
                #     visited[ni][nj] = 1
                #     s.append([ni, nj])
                #     total += 1
    return temp


def check(g):
    # print(g)
    global maxV
    cnt = 0
    temp = set()
    for i in g:
        x, y = i
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if cnt > 2:
                    return False
                elif board[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    temp.add((nx, ny))
                    cnt += 1
    if cnt == 1:
        one.append(len(g))
    elif cnt == 2:
        two.append([temp, len(g)])
    else:
        maxV += len(g)
    return True


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
group = []
temp = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 2 and visited[i][j] == 0:
            visited[i][j] = 1
            group.append(f(i, j))

maxV = 0
# print(group)
visited = [[0] * M for _ in range(N)]
# group = sorted(group, key=lambda x:len(x), reverse=True)
one = []
two = []
for i in range(len(group)):
    check(group[i])
one.sort(reverse=True)
if len(one) > 1:
    a = sum(one[0:1])
else:
    a = sum(one)
b = 0
for i in range(len(two)):
    temp = two[i][1]
    for j in range(i+1, len(two)):
        if two[i][0] == two[j][0]:
            temp += two[j][1]
        if b < temp:
            b = temp
    if b<temp:
        b = temp
print(max(a, b) + maxV)
