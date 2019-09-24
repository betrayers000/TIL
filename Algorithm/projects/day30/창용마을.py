import sys

sys.stdin = open('chang.txt', 'r')

def f(n):
    if n == p[n]:
        return n
    else:
        return f(p[n])


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    p = list(range(N+1))
    for _ in range(M):
        s, e = map(int, input().split())
        f1, f2 = f(s), f(e)
        if f1 != f2:
            p[f1] = f2
    for i in range(N+1):
        if p[i] != f(p[i]):
            p[i] = f(p[i])
    print("#{} {}".format(t, len(set(p[1:]))))
