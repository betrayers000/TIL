N = 10

def f(n, k):
    global N
    if n == N-1:
        print(res)
        return
    else:
        if res[n] + 1 < N:
            res[n+1] = res[n]+1
            f(n+1, k)
        elif res[n] -1 > N:
            res[n + 1] = res[n] -1
            f(n + 1, k)

nums = [0] * 10
res = [0] * N
for i in range(1, 10):
    res[0] = i
    f(0, N)