import sys

sys.stdin = open('wine.txt', 'r')

N = int(input())
dp = [0] * (N + 1)
wine = [0] + [int(input()) for _ in range(N)]
for i in range(1, N + 1):
    dp[i] = max(dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i])
    dp[i] = max(dp[i], dp[i-1])
print(dp[-1])
