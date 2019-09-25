import sys

sys.stdin = open('mst.txt', 'r')


def f(n):
    while n != p[n]:
        n = p[n]
    return n


V, E = map(int, input().split())
edge = []
p = list(range(V + 1))
for _ in range(E):
    edge.append(list(map(int, input().split())))

edge.sort(key=lambda x: x[2])
# 대표원소 탐색
total = 0
cnt = 0
for i in range(E):
    if cnt == V-1:
        break
    s, e, w = edge[i]
    f1, f2 = f(s), f(e)
    if f1 != f2:
        p[f1] = f2
        total += w
        cnt += 1
print(total)
