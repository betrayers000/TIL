import sys

sys.stdin = open('snake.txt', 'r')

def move(point, dir):
    x, y = point
    x_, y_ = 0, 0
    board[x][y] = 3
    if dir == 1:
        x_ = x
        y_ = y +1
    elif dir == 3:
        x_ = x
        y_ = y-1
    elif dir == 2:
        x_ = x+1
        y_ = y
    elif dir == 4:
        x_ = x-1
        y_ = y
    if 0<= x_ < N and 0<= y_ < N:
        if board[x_][y_] == 3:
            return -1, -1
        if board[x_][y_] != 1:
            board[x][y] = 0
        board[x_][y_] = 3
        return x_, y_
    return -1, -1



N = int(input())
K = int(input())
board = [[0]* N for n in range(N)]
for k in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1
L = int(input())
s = 0
start = [0, 0]
dir = 1
check = True
for i in range(L):
    x, c = input().split()
    while s < int(x):
        s += 1
        start = move(start, dir)
        if start[0] == -1:
            check = False
            break
    if not check:
        break
    if c == "L":
        if dir == 1:
            dir = 4
        else:
            dir -= 1
    elif c == "D":
        if dir == 4:
            dir = 1
        else:
            dir += 1
while check:
    s += 1
    start = move(start, dir)
    if start[0] == -1:
        check = False
        break
print(s)


