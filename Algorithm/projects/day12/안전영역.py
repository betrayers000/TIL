import sys

sys.stdin = open('safe.txt', 'r')


def bfs(x, y, i, sample):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = [0] * N*N
    front, rear = -1, -1
    rear += 1
    q[rear] = [x, y]
    sample[x][y] = 1
    while front != rear:
        front += 1
        x_, y_ = q[front]
        for z in range(4):
            nx = x_ + dx[z]
            ny = y_ + dy[z]
            if 0<= nx < N and 0<= ny < N:
                if board[nx][ny] > i and sample[nx][ny] == 0:
                    sample[nx][ny] = 1
                    rear += 1
                    q[rear] = [nx, ny]



N = int(input())
board = [list(map(int, input().split())) for n in range(N)]

max_cnt = 0
for i in range(101):
    sample = [[0] * N for n in range(N)]
    cnt = 0
    for x in range(N):
        for y in range(N):
            if board[x][y] > i and sample[x][y] == 0:
                bfs(x, y, i, sample)
                cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt
print(max_cnt)


