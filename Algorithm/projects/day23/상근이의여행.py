import sys

sys.stdin = open('travel.txt', 'r')


# union find
def f(n):
    if n == tree[n]:
        return n
    else:
        return f(tree[n])


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    tree = [i for i in range(N+1)]
    # e = [list(map(int, input().split())) for _ in range(M)]
    cnt = 0
    for _ in range(M):
        a, b = map(int, input().split())
        if tree[b] == b:
            tree[b] = f(a)
        else:
            tree[a] = f(b)
    print(tree)
    print(cnt)

