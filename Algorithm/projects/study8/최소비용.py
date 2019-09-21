import sys

sys.stdin = open('dijk.txt', 'r')


def dijk(x, y):
    global N
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = [0] * 100000
    front, rear = -1, -1
    rear += 1
    q[rear] = [x, y]
    # q = []
    # q.append([x, y])
    visited[x][y] = 0
    while front != rear:
        front += 1
        i, j = q[front]
        # i, j = q.pop(0)
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni < N and 0 <= nj < N:
                n = 0
                if board[i][j] < board[ni][nj]:
                    n = board[ni][nj] - board[i][j]
                next_ = visited[i][j] + 1 + n
                if next_ <= visited[ni][nj]:
                    visited[ni][nj] = next_
                    rear += 1
                    q[rear] = [ni, nj]
                    # q.append([ni, nj])

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[99] * N for _ in range(N)]
    dijk(0, 0)
    print("#{} {}".format(t, visited[N-1][N-1]))
