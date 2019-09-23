import sys

sys.stdin = open('tr.txt', 'r')

def find(n):
    while n != p[n]:
        n = p[n]
    return n


T = int(input())
res = []
for t in range(1, T+1):
    N, M = map(int, input().split())
    p = [i for i in range(N+1)]
    cnt = 0
    for i in range(M):
        if cnt == N-1:
            break
        n1, n2 = map(int, input().split())
        f1, f2 = find(n1), find(n2)
        if f1 != f2:
            p[f1] = f2
            cnt += 1
    res.append(str(cnt))
print('\n'.join(res))
