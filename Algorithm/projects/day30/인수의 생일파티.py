import sys

sys.stdin = open('insu.txt', 'r')

def f(n):
    for i in range(len(table[n])):
        x, w = table[n][i]
        d[x] = min(d[x], d[n] + w)

def af(n):
    for i in range(len(table)):
        for j in range(len(table[i])):
            x, w = table[i][j]
            if x == n:
                a[i] = min(a[i], a[n] +w)

T = int(input())
for t in range(1, T+1):
    N, M, X = map(int, input().split())
    table = [[]]
    for _ in range(N+1):
        table += [[]].copy()
    for _ in range(M):
        s, e, w = map(int, input().split())
        table[s].append([e, w])
    d = [999999] * (N+1)
    a = [999999] * (N+1)
    visited = [0] * (N+1)
    visited_ = [0] * (N+1)
    d[X] = 0
    a[X] = 0
    while 1:
        minV = 999999
        min_ = 0
        minA = 999999
        min_a = 0
        for i in range(N+1):
            if d[i] != 999999 and visited[i] == 0:
                if minV > d[i]:
                    minV = d[i]
                    min_ = i
            if a[i] != 999999 and visited_[i] == 0:
                if minA > a[i]:
                    minA = a[i]
                    min_a = i
        f(min_)
        af(min_a)
        visited[min_] = 1
        visited_[min_a] = 1
        if sum(visited[1:]) == N and sum(visited_[1:]) == N:
            break
    res = 0
    for i in range(1, N+1):
        if a[i] != 999999 and d[i] != 999999:
            if res < a[i] + d[i]:
                res = a[i] + d[i]
    print(a, d)
    print(res)