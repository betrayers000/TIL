import sys

sys.stdin = open('happy.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    dp = [[0] * (N+1) for _ in range(M+1)]
    for i in range(1, M+1):
        s, p = map(int, input().split())
        for j in range(1, N+1):
            if j-s >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-s] + p)
            else:
                dp[i][j] = dp[i-1][j]
    maxV = 0
    for _ in range(M+1):
        if maxV < max(dp[_]):
            maxV = max(dp[_])
    print("#{} {}".format(t, maxV))
