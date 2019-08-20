import sys

sys.stdin = open("input.txt", "r")


def checkmove(start):
    global N
    global board
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    temp = []
    x_, y_ = start
    board[x_][y_] = 1
    for i in range(4):
        x = x_ + di[i]
        y = y_ + dj[i]
        if 0 <= x < N and 0 <= y < N:
            if board[x][y] == "0":
                temp.append((x, y))
            elif board[x][y] == "3":
                temp = [0]
                break
    return temp


for t in range(1, 11):
    tc = int(input())
    N = 100
    board = [list(input()) for n in range(N)]
    start = (1, 1)
    stack = [start]
    while True:
        if stack == []:
            result = 0
            break
        temp = checkmove(start)
        if temp != []:
            if temp[0] == 0:
                result = 1
                break
            if len(temp) >= 2:
                stack.append(start)
            start = temp.pop()
        else:
            start = stack.pop()

    print(result)




