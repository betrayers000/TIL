import sys

sys.stdin = open('swim.txt', 'r')
#
# def f(n, s):
#     global d, m1, m3, minV
#
#     if n >= 13:
#         if minV > s:
#             minV = s
#         return
#     elif s > minV:
#         return
#     else:
#         f(n+1, s+d*month[n])
#         f(n+1, s+m1)
#         f(n+3, s+m3)
#

T = int(input())
for t in range(1, T+1):
    d, m1, m3, y = list(map(int, input().split()))
    month = [0] + list(map(int, input().split()))
    dp = [0] * 13
    for i in range(1, 13):
        if i < 3:
            dp[i] = dp[i-1] + min(d*month[i], m1)
        else:
            dp[i] = min((dp[i - 1] + min(d * month[i], m1)), dp[i-3] + m3)

    result = dp[-1]
    if y < dp[-1]:
        result = y







