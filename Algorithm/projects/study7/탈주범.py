import sys

sys.stdin = open('input.txt', 'r')

check = [[1, 3, 6, 7], [1, 2, 4, 7], [1, 3, 4, 5], [1, 2, 5, 6]]


# 우 하 좌 상

def move(x, y, shape, N):
    global visited
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    temp = []
    if shape == 1:
        for z in range(4):
            x_ = x + dx[z]
            y_ = y + dy[z]
            if 0 <= x_ < N and 0 <= y_ < M:
                if visited[x_][y_] == 0 and board[x_][y_] in check[z]:
                    visited[x_][y_] = visited[x][y] + 1
                    temp.append([x_, y_])
    elif shape == 2:
        for z in range(1, 4, 2):
            x_ = x + dx[z]
            y_ = y + dy[z]
            if 0 <= x_ < N and 0 <= y_ < M:
                if visited[x_][y_] == 0 and board[x_][y_] in check[z]:
                    visited[x_][y_] = visited[x][y] + 1
                    temp.append([x_, y_])
    elif shape == 3:
        for z in range(0, 4, 2):
            x_ = x + dx[z]
            y_ = y + dy[z]
            if 0 <= x_ < N and 0 <= y_ < M:
                if visited[x_][y_] == 0 and board[x_][y_] in check[z]:
                    visited[x_][y_] = visited[x][y] + 1
                    temp.append([x_, y_])
    elif shape == 4:
        for z in range(0, 4, 3):
            x_ = x + dx[z]
            y_ = y + dy[z]
            if 0 <= x_ < N and 0 <= y_ < M:
                if visited[x_][y_] == 0 and board[x_][y_] in check[z]:
                    visited[x_][y_] = visited[x][y] + 1
                    temp.append([x_, y_])
    elif shape == 5:
        for z in range(2):
            x_ = x + dx[z]
            y_ = y + dy[z]
            if 0 <= x_ < N and 0 <= y_ < M:
                if visited[x_][y_] == 0 and board[x_][y_] in check[z]:
                    visited[x_][y_] = visited[x][y] + 1
                    temp.append([x_, y_])
    elif shape == 6:
        for z in range(1, 3):
            x_ = x + dx[z]
            y_ = y + dy[z]
            if 0 <= x_ < N and 0 <= y_ < M:
                if visited[x_][y_] == 0 and board[x_][y_] in check[z]:
                    visited[x_][y_] = visited[x][y] + 1
                    temp.append([x_, y_])
    elif shape == 7:
        for z in range(2, 4):
            x_ = x + dx[z]
            y_ = y + dy[z]
            if 0 <= x_ < N and 0 <= y_ < M:
                if visited[x_][y_] == 0 and board[x_][y_] in check[z]:
                    visited[x_][y_] = visited[x][y] + 1
                    temp.append([x_, y_])
    return temp


def bfs(start, N, M):
    q = [0] * (N * M)
    front, rear = -1, -1
    rear += 1
    q[rear] = start
    while front != rear:
        front += 1
        x, y = q[front]
        next_ = move(x, y, board[x][y], N)
        for i in next_:
            rear += 1
            q[rear] = i


T = int(input())
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    visited = [[0] * M for _ in range(N)]
    board = [list(map(int, input().split())) for _ in range(N)]
    start = [R, C]
    visited[R][C] = 1
    bfs(start, N, M)
    print(visited)
    total = 0
    for b in visited:
        for i in b:
            if i <= L and i != 0:
                total += 1
    print(total)
