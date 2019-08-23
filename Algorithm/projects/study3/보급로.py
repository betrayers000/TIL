import sys

sys.stdin = open('input.txt', 'r')

def bfs(point, N):
    q = [0] * (N*N)
    front, rear = -1, -1
    rear += 1
    q[rear] = point
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[0]*N for n in range(N)]
    while True:
        if front == rear:
            break
        front += 1
        x, y = q[front]
        for k in range(4):
            x_ = x + dx[k]
            y_ = y + dy[k]
            if 0<= x_ < N and 0<= y_ < N:
                if visited[x_][y_] = 0:





start = [0, 0]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(input()) for n in range(N)]

