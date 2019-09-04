import sys

sys.stdin = open('supply.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [input() for _ in range(N)]
    sample = [[9 * (N * N)] * N for _ in range(N)]
    sample[0][0] = int(board[0][0])
    q = []
    q.append([0, 0])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while q != []:
        x, y = q.pop(0)
        for k in range(4):
            x_ = x + dx[k]
            y_ = y + dy[k]
            if 0 <= x_ < N and 0 <= y_ < N:
                if int(sample[x][y]) + int(board[x_][y_]) < sample[x_][y_]:
                    q.append([x_, y_])
                    sample[x_][y_] = int(sample[x][y]) + int(board[x_][y_])
    print(sample[-1][-1])
