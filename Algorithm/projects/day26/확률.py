import sys

sys.stdin = open('input.txt', 'r')


def f(n, k):
    global cnt
    if n == k:
        if p[0] != 0:
            cnt += 1
        return
    else:
        for i in range(10):
            if used[i] == 0:
                p[n] = i
                used[i] = 1
                f(n + 1, k)
                used[i] = 0


T = int(input())
nums = list(range(10))
for t in range(1, T + 1):
    N = int(input())
    a = 10 ** N - 10 ** (N - 1)
    p = [0] * N
    used = [0] * 10
    cnt = 0
    f(0, N)
    print(cnt)
