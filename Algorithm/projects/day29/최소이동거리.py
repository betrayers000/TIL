import sys

sys.stdin = open('dis.txt', 'r')


def f(n):
    global table, d, N
    for i in range(N + 1):
        if table[n][i] != 0:
            d[i] = min(d[i], d[n] + table[n][i])


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(M)]
    table = [[0] * (N + 1) for _ in range(N + 1)]
    for eg in edge:
        n1, n2, w = eg
        table[n1][n2] = w
    d = [9999] * (N + 1)
    visited = [0] * (N + 1)
    d[0] = 0
    while 1:
        minV = 9999
        minI = 0
        for j in range(N + 1):
            if d[j] != 9999 and visited[j] == 0:
                if minV > d[j]:
                    minI = j
                    minV = d[j]
        f(minI)
        visited[minI] = 1
        if visited[-1] == 1:
            break
    print("#{} {}".format(t, d[-1]))
