import sys
import timeit

sys.stdin = open('nq.txt', 'r')

def check(n):
    global used, p, N
    used = [0] * N
    n = n + 1
    for i in p[::-1]:
        if i == 0:
            continue
        else:
            z = n - i[0]
            if 0 <= i[1] + z < N:
                used[i[1] + z] = 1
            if 0 <= i[1] - z < N:
                used[i[1] - z] = 1
            used[i[1]] = 1


def f(n, k):
    global p, cnt
    if n == k:
        cnt += 1
        return
    else:
        for i in range(k):
            if used[i] == 0:
                p[n] = [n, i]
                check(n)
                f(n + 1, k)
                p[n] = 0
                check(n - 1)

start = timeit.default_timer()
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    p = [0] * N
    used = [0] * N
    cnt = 0
    f(0, N)
    print(f"#{t} {cnt}")
end = timeit.default_timer()
print(end - start)