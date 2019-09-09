import sys

sys.stdin = open('search.txt', 'r')


N = int(input())
par = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    if a == 1:
        par[b] = a
    elif b == 1:
        par[a] = b
    else:
        if par[a] == 0:
            par[a] = b
        else:
            par[b] = a
for i in range(len(par)):
    if par[i] != 0:
        print(par[i])