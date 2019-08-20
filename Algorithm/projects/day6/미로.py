import sys

sys.stdin = open("input.txt", "r")

def checkmove(start, exp):
    global N
    global board
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    temp = []
    x_, y_ = start
    for i in range(4):
        x = x_ + di[i]
        y = y_ + dj[i]
        if 0 <= x < N and 0 <= y < N:
            if board[x][y] == "0":
                if not (x, y) in exp:
                    temp.append((x, y))
            elif board[x][y] == "3":
                temp = [0]
                break
    return temp



T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(input()) for i in range(N)]
    start = ()
    end = ()
    for i in range(N):
        for j in range(N):
            if board[i][j] == "2":
                start = (i, j)
            elif board[i][j] == "3":
                end = (i, j)
    start_list = [start]
    exp = []
    while True:
        if start_list == []:
            break
        next_ = checkmove(start, exp)
        if next_ == [0]:
            exp = [3]
            break
        if next_ == []:
            start = start_list.pop()
        else:
            start = next_.pop()
        start_list.extend(next_)
        exp.append(start)
    if exp[0] == 3:
        print(f"#{t} {1}")
    else:
        print(f"#{t} {0}")





