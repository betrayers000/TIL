N = 100

def f(n, k):
    global N
    if n == N-1:
        return
    else:
        if res[n] + 1 < 10:
            res[n+1] = res[n]+1
            nums[res[n+1]] += 1
            f(n+1, k)
            nums[res[n + 1]] -= 1
        if res[n] - 1 >= 0:
            res[n + 1] = res[n] -1
            nums[res[n + 1]] += 1
            f(n + 1, k)
            nums[res[n + 1]] -= 1

nums = [0] * 10
res = [0] * N
for i in range(1, 10):
    res[0] = i
    nums[i] = 1
    f(0, N)
    nums[i] = 0