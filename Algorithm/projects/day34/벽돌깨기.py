import sys

sys.stdin = open('block.txt', 'r')


def f(n, k, m):
    global maxV
    if n == m:
        board = make_temp_board()
        for i in range(len(p)):
            drop(p[i], board)
            board = down_block(board)
        res = count_board(board)
        if maxV > res:
            maxV = res
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
            if board[i][j] != 0:
                cnt += 1
    return cnt

def drop(n, board):
    global H, W
    cp = 0
    cs = 0
    for i in range(H):
        if board[i][n] >= 1:
            cp = i
            cs = board[i][n]
            break
    check_block(cp, n, cs, board)


def check_block(i, j, n, board):
    # 왼쪽 0, -1
    # print(n)
    temp = j -1
    board[i][j] = 0
    while temp >= j - n + 1:
        if temp < 0 or temp >= W:
            break
        if board[i][temp] == 1:
            board[i][temp] = 0
        elif board[i][temp] > 1:
            te = board[i][temp]
            # board[i][temp] = 0
            check_block(i, temp, te, board)
        temp -= 1
    temp = j +1
    # 오른쪽 0, 1
    while temp <= j + n - 1:
        if temp < 0 or temp >= W:
            break
        if board[i][temp] == 1:
            board[i][temp] = 0
        elif board[i][temp] > 1:
            te = board[i][temp]
            # board[i][temp] = 0
            check_block(i, temp, te, board)
        temp += 1
    temp = i + 1
    # 아래 +1, 0
    while temp <= i + n - 1:
        if temp <= 0 or temp >= H:
            break
        if board[temp][j] == 1:
            board[temp][j] = 0
        elif board[temp][j] > 1:
            te = board[temp][j]
            # board[temp][j] = 0
            check_block(temp, j, te, board)
        temp += 1
    temp = i - 1
    while temp >= i - n + 1:
        if temp <= 0 or temp >= H:
            break
        if board[temp][j] == 1:
            board[temp][j] = 0
        elif board[temp][j] > 1:
            te = board[temp][j]
            # board[temp][j] = 0
            check_block(temp, j, te, board)
        temp -= 1


def make_temp_board():
    temp = []
    for i in range(len(ori_board)):
        temp.append(ori_board[i].copy())
    return temp

def down_block(board):
    global H, W
    for i in range(H-1, 0, -1):
        for j in range(W):
            temp = i
            if board[temp][j] != 0:
                tempV = board[temp][j]
                board[temp][j] = 0
                while board[temp][j] == 0:
                    temp += 1
                    if temp >= H:
                        break
                if board[temp-1][j] == 0:
                    board[temp-1][j] = tempV
    return board


T = int(input())
for t in range(1, T+1):
    N, W, H = map(int, input().split())
    ori_board = [list(map(int, input().split())) for _ in range(H)]
    start_point = list(range(W))
    maxV = 9999999
    p = [0] * N
    f(0, W, N)  # 구슬의 시작위치 선택
    print(maxV)