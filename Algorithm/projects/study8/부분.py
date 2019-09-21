import sys

sys.stdin = open('set.txt', 'r')

# def f(n, k, m, z, s):
#     global cnt, K
#     if n == m:
#         if s == K:
#             cnt += 1
#         return
#     else:
#         for i in range(z, k):
#             if used[i] == 0:
#                 used[i] = 1
#                 p[n] = nums[i]
#                 f(n+1, k, m, i, s+nums[i])
#                 used[i] = 0
def f(n, k, m, s):
    global cnt
    if n == k:
        if s == m:
            cnt += 1
        return
    else:
        p[n] = 0
        f(n+1, k, m, s+nums[n])
        p[n] = 1
        f(n+1, k, m, s)


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    nums = list(map(int, input().split()))
    # for i in range(1,N+1):
    #     p = [0] * i
    #     used = [0] *N
    #     f(0, N, i, 0, 0)
    p = [0] * N
    f(0, N, K, 0)
    print(cnt)