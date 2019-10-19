import sys
sys.stdin = open('wine.txt', 'r')

N = int(input())
wine = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N+1)
for i in range(1, N+1):
    if i < 3:
        dp[i] = dp[i-1] + wine[i]
    else:
        dp[i] = max(dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i])
print(max(dp))