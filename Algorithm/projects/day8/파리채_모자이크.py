import sys

sys.stdin = open('fly.txt', 'r')

def getfly(x, y, M):
    point = []
    for i in range(M):
        x_ = x+i
        for j in range(1, M//2+1):
            if i%2:
                point.append([x_, y+j])
            else:
                point.append()


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(N)]
    total_ = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = getfly_cross(i, j, M)
            if total_ < total:
                total_ = total
    print(total_)