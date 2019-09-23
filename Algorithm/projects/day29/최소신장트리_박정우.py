import sys

sys.stdin = open('mst.txt', 'r')

def find(n):
    if n == p[n]:
        return n
    else:
        return find(p[n])

T = int(input())
for t in range(1, T + 1):
    N, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    edge = sorted(edge, key=lambda x: x[2])
    # 사이클 방지
    total = 0
    p = list(range(N + 1))
    cnt = 0
    for eg in edge:
        n1, n2, w = eg
        if cnt == N:
            break
        if find(n1) != find(n2):
            total += w
            p[find(n1)] = find(n2)
            cnt += 1
    print(total)
