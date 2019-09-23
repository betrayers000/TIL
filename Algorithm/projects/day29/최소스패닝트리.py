import sys

sys.stdin = open('mst.txt', 'r')

def find(n):
    while p[n] != n:
        n = p[n]
    return n

N, E = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(E)]
edge = sorted(edge, key=lambda x: x[2])
# 사이클 방지
total = 0
p = list(range(N + 1))
cnt = 0
for eg in edge:
    n1, n2, w = eg
    if cnt == N-1:
        break
    f1, f2 = find(n1), find(n2)
    if f1 != f2:
        total += w
        p[f1] = f2
        cnt += 1
print(total)