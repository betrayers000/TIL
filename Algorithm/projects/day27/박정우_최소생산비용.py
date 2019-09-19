def per(n, k, total):
    global ans
    if n == k:
        if total < ans:
            ans = total
        return
    elif total > ans:
        return
    else:
        for i in range(k):
            if used[i] == 0:
                temp[n] = table[n][i]
                used[i] = 1
                per(n+1, k, total + table[n][i])
                used[i] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for n in range(N)]
    ans = 300
    used = [0] * N
    temp = [0] * N
    per(0, N, 0)
    print("#{} {}".format(t, ans))