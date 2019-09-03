import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
dp = [0] * (N+1)
stair = [0] + [int(input()) for _ in range(N)]
for i in range(1, N+1):
    if i < 3:
        dp[i] = dp[i-1] + stair[i]
    else:
        dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i] + stair[i-1])
print(dp[-1])

