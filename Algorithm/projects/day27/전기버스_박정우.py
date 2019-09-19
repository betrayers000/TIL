import sys

sys.stdin = open('bus.txt', 'r')

def f(n, k, s, c):
    global minV, M
    if s < 0 or c > minV:
        return
    if n == k:
        if minV > c:
            minV = c
        return
    else:
        f(n + 1, k, M[n] - 1, c + 1)
        f(n + 1, k, s - 1, c)

T = int(input())
for t in range(1, T + 1):
    inp = list(map(int, input().split()))
    N = inp[0]
    M = [0] + inp[1:]
    minV = 999
    f(1, N, 0, 0)
    print("#{} {}".format(t, minV-1))
