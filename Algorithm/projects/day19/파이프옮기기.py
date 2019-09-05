import sys

sys.stdin = open('pipe.txt', 'r')

dx = [[0, 1], [1, 0], [1, 1]]  # 오른쪽 밑 대각선


def dfs(x, y, d):
    global board, dx, N, cnt
    if x == N-1 and y == N-1:
        cnt += 1
        return
    else:
        if d == 4:
            board[x][y] = d
            if 0 <= y - 1 < N:
                board[x][y - 1] = 1
            if 0 <= x - 1 < N:
                board[x - 1][y] = 1
            for i in range(3):
                nx = x + dx[i][0]
                ny = y + dx[i][1]
                if 0 <= nx < N and 0 <= ny < N:
                    if i == 2:
                        if board[nx-1][ny] != 1 and board[nx][ny-1] != 1 and board[nx][ny] != 1:
                            dfs(nx, ny, i+2)
                            if 0 <= ny - 1 < N:
                                board[nx][ny - 1] = 0
                            if 0 <= nx - 1 < N:
                                board[nx - 1][ny] = 0
                    else:
                        if board[nx][ny] != 1:
                            dfs(nx, ny, i+2)
                            board[nx][ny] = 0
        elif d == 2:
            board[x][y] = d
            for i in range(0, 3, 2):
                nx = x + dx[i][0]
                ny = y + dx[i][1]
                if 0 <= nx < N and 0 <= ny < N:
                    if i == 2:
                        if board[nx-1][ny] != 1 and board[nx][ny-1] != 1 and board[nx][ny] != 1:
                            dfs(nx, ny, i+2)
                            if 0 <= ny - 1 < N:
                                board[nx][ny - 1] = 0
                            if 0 <= nx - 1 < N:
                                board[nx - 1][ny] = 0
                    else:
                        if board[nx][ny] != 1:
                            dfs(nx, ny, i+2)
                            board[nx][ny] = 0
        elif d == 3:
            board[x][y] = d
            for i in range(1, 3):
                nx = x + dx[i][0]
                ny = y + dx[i][1]
                if 0 <= nx < N and 0 <= ny < N:
                    if i == 2:
                        if board[nx-1][ny] != 1 and board[nx][ny-1] != 1 and board[nx][ny] != 1:
                            dfs(nx, ny, i+2)
                            if 0 <= ny - 1 < N:
                                board[nx][ny - 1] = 0
                            if 0 <= nx - 1 < N:
                                board[nx - 1][ny] = 0
                    else:
                        if board[nx][ny] != 1:
                            dfs(nx, ny, i+2)
                            board[nx][ny] = 0


N = int(input())
board = [[0]*(N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+2)]
cnt = 0
dfs(1, 2, 2)
print(cnt)
