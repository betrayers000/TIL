import sys

sys.stdin = open("input.txt", "r")

def checkmove(x, y):
    global board
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    if board[x][y] == "2":
        return 1
    else:
        board[x][y] = "1"
        for i in range(4):
            x_ = x+di[i]
            y_ = y+dj[i]
            if 0 <= x_ < N and 0 <= y_ < N:
                if board[x_][y_] != "1":
                    if checkmove(x_, y_) == 1:
                        return 1
        return 0

for t in range(1, 11):
    tc = int(input())
    N = 16
    board = [list(input()) for n in range(N)]
    result = checkmove(13, 13)
    print(f"#{t} {result}")

