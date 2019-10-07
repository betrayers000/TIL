def f(n, k, m, z):
    if n == m:
        print(p)
        return
    else:
        for i in range(z, k):
            if used[i] == 0:
                p[n] = i
                used[i] = 1
                f(n+1, k, m, i)
                used[i] = 0

used = [0] * 4
p = [0] * 2
f(0, 4, 2, 0)