import sys

sys.stdin = open('maze.txt', 'r')


def f(i, j):
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    if arr[i][j] == '2':
        print(arr[i][j])
        return 1
    else:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 16 > ni >= 0 and 16 > nj >= 0:
                if arr[ni][nj] != '1':
                    arr[i][j] = '1'
                    if f(ni, nj) == 1:
                        return 1
                    arr[i][j] = '0'


for tc in range(1):
    t = int(input())
    arr = [list(input()) for _ in range(16)]
    for i in range(16):
        if '3' in arr[i]:
            for j in range(16):
                if arr[i][j] == '3':
                    a = f(i, j)
                    print(a)
