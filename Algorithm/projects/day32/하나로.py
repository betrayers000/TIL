import sys

sys.stdin = open('hana.txt', 'r')


def f(n):
    while p[n] != n:
        n = p[n]
    return n


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    land = list(zip(X, Y))
    edge = []
    for i in range(N):
        for j in range(i + 1, N):
            dis = abs(land[i][0] - land[j][0]) ** 2 + abs(land[i][1] - land[j][1]) ** 2
            edge.append([i, j, dis])
            edge.append([j, i, dis])
    edge.sort(key=lambda x: x[2])
    total = 0
    p = list(range(N))
    cnt = 0
    for i in range(len(edge)):
        if cnt == N-1:
            break
        s, e, w = edge[i]
        f1, f2 = f(s), f(e)
        if f1 != f2:
            p[f1] = f2
            total += w
            cnt += 1
    print("#{} {}".format(t, int(round(total * E, 0))))
