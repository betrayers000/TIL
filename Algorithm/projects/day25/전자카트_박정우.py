import sys

sys.stdin = open('cart.txt', 'r')

def f(n, k, s):
    global minV
    if n == k:
        print(p)
        if s + table[p[-2]-1][p[-1]-1] < minV:
            minV = s + table[p[-2]-1][p[-1]-1]
        return
    elif s > minV:
        return
    else:
        for i in range(k):
            if used[i] == 0:
                p[n+1] = room[i]
                used[i] = 1
                f(n+1, k, s + table[p[n]-1][p[n+1]-1])
                used[i] = 0



T = int(input())
for t in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    room = list(range(2, N+1))
    minV = 100 * (N+1)
    p = [0] * (N-1)
    p = [1] + p + [1]
    used = [0] * (N-1)
    f(0, N-1, 0)
    print(minV)
