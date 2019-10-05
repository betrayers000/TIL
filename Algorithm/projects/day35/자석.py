import sys

sys.stdin = open('magnetic.txt', 'r')
# 2, 6 >
def cycle(d, mag):
    temp = []
    if d == 1:
        temp.append(mag[7])
        for i in range(7):
            temp.append(mag[i])
    elif d == -1:
        for i in range(1, 8):
            temp.append(mag[i])
        temp.append(mag[0])
    return temp

def go(n, d):
    if d == 1:
        r = -1
    else:
        r = 1
    check(n)
    cycle(d, board[n])

def check(n):
    temp = {n-1}
    for i in range(3):
        if board[i][2] != board[i+1][6]:
            temp.add(i)
            temp.add(i+1)
        else:
            break
    group.extend(list(temp))

T = int(input())
for t in range(1, T+1):
    K = int(input())
    board = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(K):
        group = []
        n, d = map(int, input().split())
        go(n, d)
    total = 0
    sc = [1, 2, 4, 8]
    print(board)
    for i in range(4):
        if board[i][0] == 1:
            total += sc[i]
    print(total)

