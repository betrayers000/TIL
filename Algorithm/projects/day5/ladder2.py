import sys

sys.stdin = open("input.txt", "r")

# ladder1 과 같지만 가장 짧은거리 구하기
# 도착점이 전부 1이다.
def check(board, x, y, c):
    if c == 0:
        if y == 0:
            if board[x][y + 1] == 1:
                return 3
        elif y == 99:
            if board[x][y-1] == 1:
                return 2
        else:
            if board[x][y-1] == 1:
                return 2
            elif board[x][y + 1] == 1:
                return 3
    elif c == 2:
        if y > 0:
            if board[x][y-1] == 1:
                return 2
    elif c == 3:
        if y < 99:
            if board[x][y+1] == 1:
                return 3
    return 0




for t in range(1, 11):
    n = int(input())
    board = [list(map(int, input().split())) for i in range(100)]
    start = []
    stack = []
    for i in range(100):
        if board[0][i] == 1:
            start.append((0, i))
    mincnt = 10000
    minsp = 0
    for sp in start:
        x, y = sp
        c = 0
        cnt = 0
        while x != 99:
            c = check(board, x, y, c)
            if c == 2:
                y -= 1
            elif c == 3:
                y += 1
            else :
                x += 1
            end = board[x][y]
            cnt += 1
        if mincnt > cnt:
            mincnt = cnt
            minsp = sp[1]

    print(minsp)


