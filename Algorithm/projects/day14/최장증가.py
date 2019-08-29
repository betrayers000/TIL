import sys

sys.stdin = open('test.txt', 'r')


T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    dp = [1] * N
    for i in range(1, N):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)

    print(dp)