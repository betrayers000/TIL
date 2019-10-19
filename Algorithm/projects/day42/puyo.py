import sys

sys.stdin = open('puyo.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def crush(x, y, m):
    stack = [0] * (12 * 6)
    top = 0
    stack[top] = [x, y]
    color = board[x][y]
    cnt = 0
    temp = []
    while top >= 0:
        i, j = stack[top]
        top -= 1
        for k in range(4):
            ni, nj = i + dx[k], j + dy[k]
            if 0 <= ni < 12 and 0 <= nj < 6 and board[ni][nj] == color:
                board[ni][nj] = "."
                top += 1
                cnt += 1
                stack[top] = [ni, nj]
                temp.append([ni, nj])
    if cnt < 4:
        for i in temp:
            x, y = i
            board[x][y] = color
        return False
    else:
        return True


def drop():
    for i in reversed(range(12)):
        for j in range(6):
            if board[i][j] == ".":
                z = i
                while z > -1:
                    color = board[z][j]
                    if color != ".":
                        board[i][j] = color
                        board[z][j] = "."
                        break
                    z -= 1


board = [list(input()) for _ in range(12)]
res = 0
while True:
    # print(board)
    i = 0
    check = False
    while i < 12:
        for j in range(6):
            if board[i][j] != ".":
                if crush(i, j, 0):
                    check = True
        i += 1
    drop()
    if not check:
        break
    else:
        res += 1
print(res)
