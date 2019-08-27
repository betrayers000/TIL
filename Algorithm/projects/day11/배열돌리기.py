import sys

sys.stdin = open('rotation.txt', 'r')


def rotation(x1, y1, x2, y2, n, copy_board):
    temp = [0]
    nx, ny, ny_ = 0, 0, 0
    for i in range(4):
        for j in range(1, y2 - y1 + 1 - n):
            if i == 0:
                temp.append(copy_board[x1][y1 + j])
                ny = y1 + j
            elif i == 1:
                temp.append(copy_board[x1 + j][ny])
                nx = x1 + j
            elif i == 2:
                temp.append(copy_board[nx][ny - j])
                ny_ = ny - j
            elif i == 3:
                temp.append(copy_board[nx - j][ny_])
    temp[0], temp[-1] = temp[-1], temp[0]
    idx = 0
    for i in range(4):
        for j in range(1, y2 - y1 + 1 - n):
            if i == 0:
                copy_board[x1][y1 + j] = temp[idx]
                ny = y1 + j
            elif i == 1:
                copy_board[x1 + j][ny] = temp[idx]
                nx = x1 + j
            elif i == 2:
                copy_board[nx][ny - j] = temp[idx]
                ny_ = ny - j
            elif i == 3:
                copy_board[nx - j][ny_] = temp[idx]
            idx += 1



def check_point(point, copy_board):
    global board
    r, c, s = point
    x1, y1 = r - s - 1, c - s - 1
    x2, y2 = r + s - 1, c + s - 1
    for i in range((y2 - y1 + 2) // 2):
        rotation(x1 + i, y1 + i, x2, y2, i, copy_board)
    return copy_board


def per(n, k, used, temp):
    global result
    global board
    global f_sum

    if n == k:
        copy_board = []
        for b in board:
            copy_board.append(b.copy())
        for point in temp:
            check_point(point, copy_board)
        for copy_ in copy_board:
            if f_sum > sum(copy_):
                f_sum = sum(copy_)
        return
    else:
        for i in range(k):
            if used[i] == 0 :
                temp[n] = rotations[i]
                used[i] = 1
                per(n+1, k, used, temp)
                used[i] = 0
                temp[n] = 0
        return



N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for n in range(N)]
rotations = [list(map(int, input().split())) for k in range(K)]
used = [0] * K
temp = [0] * K
result = []
f_sum = sum(board[0])

per(0, K, used, temp)
print(f_sum)