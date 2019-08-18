import sys

sys.stdin = open("input.txt", "r")


def makeline(x1, y1, x2, y2, x3, y3):
    result = []
    temp = []
    for x in range(N):
        temp.append(board[x1-x][y1])
    result.append(''.join(map(str, temp)))
    temp = []
    for y in range(N):
        temp.append(board[x2][y2-y])
    result.append(''.join(map(str, temp)))
    temp=[]
    for z in range(N):
        temp.append(board[x3+z][y3])
    result.append(''.join(map(str, temp)))
    return result




T = int(input())
for t in range(1, 1+T):
    N = int(input())
    board = [[int(i) for i in input().split()] for n in range(N)]
    result = []
    for j in range(N):
        x1, y1 = N - 1, 0
        x2, y2 = N - 1, N - 1
        x3, y3 = 0, N - 1
        y1 += j
        x2 -= j
        y3 -= j
        temp = makeline(x1, y1, x2, y2, x3, y3)
        result.append(temp)
    print(result)
