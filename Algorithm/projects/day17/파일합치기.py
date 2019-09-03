import sys

sys.stdin = open('file.txt', 'r')

T = int(input())
for t in range(1, T+1):
    K = int(input())
    nums = [0] + list(map(int, input().split()))
    dp = [0] * (K+1)
    for i in range(3, K+1):
        a = nums[i-2] + nums[i-1]
        b = nums[i-1] + nums[i]
        if min(a, b) == a:
            dp[i] = dp[i-3] + a + nums[i]
            dp[i-1] = a
        else:
            dp[i] = dp[i - 3] + b + nums[i]
            dp[i - 1] = b

    print(dp)


