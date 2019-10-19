import sys

sys.stdin = open('shark.txt', 'r')

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
size = 2
feed = 0

def f(temp, s):
    global size, feed
    temp.sort(key=lambda x:x)
    print(temp, size)
    q = [0] * (N*N)
    front, rear = -1, -1
    rear += 1
    q[rear] = temp[0]
    visited = [[0] * N for _ in range(N)]
    able = []
    visited[temp[0][0]][temp[0][1]] = 1
    board[temp[0][0]][temp[0][1]] = 0
    minV = 99999
    while front != rear:
        front += 1
        x, y = q[front]
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0<= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and board[nx][ny] <= size:
                visited[nx][ny] = visited[x][y] + 1
                rear += 1
                q[rear] = [nx, ny]
                if board[nx][ny] != 0 and board[nx][ny] < size:
                    if minV > visited[nx][ny]:
                        minV = visited[nx][ny]
                        able = [[nx, ny]]
                    elif minV == visited[nx][ny]:
                        able.append([nx, ny])
    if able == []:
        return s
    feed += 1
    if feed == size:
        size += 1
        feed = 0
    res = f(able, s + visited[able[0][0]][able[0][1]]-1)
    if res != 0:
        return res
    return 0

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
shark = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark.append([i, j])
print(f(shark, 0))
