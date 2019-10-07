import sys

sys.stdin = open('maze.txt')

dx = [0, 1, 0, -1, 0, 0]
dy = [1, 0, -1, 0, 0, 0]


def bfs(i, j, z, temp):
    global minV
    q = [0] * 200
    front, rear = -1, -1
    rear += 1
    q[rear] = [i, j, z]
    visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    visited[z][i][j] = 1
    while front != rear:
        front += 1
        x, y, h = q[front]
        if visited[h][x][y] >= minV:
            return -1
        for k in range(6):
            nh = h
            nx = x + dx[k]
            ny = y + dy[k]
            if k == 4:
                nh = h + 1
            elif k == 5:
                nh = h - 1
            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nh < 5 and visited[nh][nx][ny] == 0 and temp[nh][nx][ny] == 1:
                if nh == 4 and ny == 4 and nx == 4:
                    return visited[h][x][y]
                rear += 1
                q[rear] = [nx, ny, nh]
                visited[nh][nx][ny] = visited[h][x][y] + 1
    return -1


def f(n, k, pos):
    global minV
    if n == k:
        temp = make_temp(pos)
        check = False
        for i in range(5):
            turn_temp = turn(i, p[i], temp[i])
            if turn_temp != temp[i]:
                check = True
            temp[i] = turn_temp
        if temp[0][0][0] == 1 and temp[4][4][4] == 1:
            if check or minV == 999999:
                res = bfs(0, 0, 0, temp)
                if minV > res and res != -1:
                    minV = res
    else:
        for i in range(4):
            p[n] = i
            f(n + 1, k, pos)


def turn(h, d, board):
    temp = [[], [], [], [], []]
    for k in range(d):
        for i in range(5):
            for j in range(4, -1, -1):
                temp[i].append(board[j][i])
        board = temp
        temp = [[], [], [], [], []]
        # temp = [[]]
        # for _ in range(4):
        #     temp += [[]].copy()
    return board


def make_temp(pos):
    temp = [[], [], [], [], []]
    # for _ in range(4):
    #     temp += [[]].copy()
    for i in range(5):
        for j in range(5):
            temp[pos[i]].append(maze[i][j])
    return temp


def fn(n, k):
    if n == k:
        f(0, 5, pn)
        return
    else:
        for i in range(5):
            if used[i] == 0:
                pn[n] = i
                used[i] = 1
                fn(n + 1, k)
                used[i] = 0


maze = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
p = [0] * 5
pn = [0] * 5
used = [0] * 5
minV = 999999
fn(0, 5)
if minV == 999999:
    minV = -1
print(minV)
