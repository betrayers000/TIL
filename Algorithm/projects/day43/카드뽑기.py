N = int(input())
price = list(map(int, input().split()))
value = {}
dp = [[0] * N for _ in range(N)]
for idx, val in enumerate(price):
    value[idx] = val/(idx+1)
for i in range(N):
    for j in range(N):
        dp[i][j] = max(dp[i-1][j-1] + value[i], value[i]*(j+1))

maxV = 0
for i in range(N):
    if dp[i][-1] > maxV:
        maxV = dp[i][-1]

print(dp)
print(int(maxV))