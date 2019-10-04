import sys

sys.stdin = open('block.txt', 'r')


def f(n, k, m):
    global maxV
    if maxV == 0:
        return
    if n == m:
        # print(p)
        board = make_temp_board()
        for i in p:
            drop(i, board)
            board = down_block(board)
        res = count_board(board)
        if maxV > res:
            maxV = res
        del board
        return
    else:
        for i in range(k):
            p[n] = i
            f(n + 1, k, m)


def count_board(board):
    global W, H
    cnt = 0
    for i in range(H):
        for j in range(W):
            if board[i][j] > 0:
                cnt += 1
    return cnt


def drop(n, board):
    global H, W
    for i in range(H):
        if board[i][n] > 0:
            # print(board[i][n])
            return check_block(i, n, board[i][n], board)


def check_block(i, j, n, board):
    global W, H
    # 왼쪽 0, -1
    # print(n)
    # temp = j - 1
    board[i][j] = 0
    for x in range(j-1, j - n, -1):
        if 0 <= x < W:
            if board[i][x] == 1:
                board[i][x] = 0
            elif board[i][x] > 1:
                check_block(i, x, board[i][x], board)
                # break
    for x in range(j+1, j + n):
        if 0 <= x < W:
            if board[i][x] == 1:
                board[i][x] = 0
            elif board[i][x] > 1:
                check_block(i, x, board[i][x], board)
                # break
    for x in range(i+1, i + n):
        if 0 <= x < H:
            if board[x][j] == 1:
                board[x][j] = 0
            elif board[x][j] > 1:
                check_block(x, j, board[x][j], board)
                # break
    # 아래 +1, 0
    for x in range(i-1, i - n, -1):
        if 0 <= x < H:
            if board[x][j] == 1:
                board[x][j] = 0
            elif board[x][j] > 1:
                check_block(x, j, board[x][j], board)
                # break
    return 0

def make_temp_board():
    temp = []
    for i in range(len(ori_board)):
        temp.append(ori_board[i].copy())
    return temp


def down_block(board):
    global H, W
    for i in range(H - 1, -1, -1):
        for j in range(W):
            temp = i
            if board[temp][j] != 0:
                tempV = board[temp][j]
                board[temp][j] = 0
                while board[temp][j] == 0:
                    temp += 1
                    if temp >= H:
                        break
                if temp - 1 < H:
                    board[temp - 1][j] = tempV
    return board


T = int(input())
for t in range(1, 2):
    N, W, H = map(int, input().split())
    ori_board = [list(map(int, input().split())) for _ in range(H)]
    start_point = list(range(W))
    maxV = 9999999
    p = [0] * N
    f(0, W, N)  # 구슬의 시작위치 선택
    print("#{} {}".format(t, maxV))
