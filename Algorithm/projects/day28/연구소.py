import sys

sys.stdin = open('virus.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(start):
    global N, M
    visited = [[0] * M for _ in range(N)]
    q = [0] * (N * M)
    front, rear = -1, -1
    rear += 1
    for s in start:
        q[rear] = s
    while front != rear:
        front += 1
        x, y = q[front]
        visited[x][y] = 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and area[nx][ny] == 0:
                    rear += 1
                    q[rear] = [nx, ny]


N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
# 벽세우기 -> 탐색 -> 최소값 찾기
start = []
for i in range(N):
    for j in range(M):
        if area[i][j] == 2:
            start.append([i, j])
        if area[i][j] == 0 and (i <= N - 1 and j <= M - 3):
            for i2 in range(N):
                for j2 in range(M):
                    if i == i2 and j2 <= j:
                        continue
                    if area[i2][j2] == 0 and (i2 <= N - 1 and j2 <= M - 2):
                        for i3 in range(N):
                            for j3 in range(M):
                                if i2 == i3 and j3 <= j2:
                                    continue
                                if area[i3][j3] == 0:
                                    area[i][j] = 1
                                    area[i2][j2] = 1
                                    area[i3][j3] = 1
                                    bfs(start)
