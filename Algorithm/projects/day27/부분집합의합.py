import sys

sys.stdin = open('setsum.txt', 'r')

def f(n, k, s, t):
    global K, cnt
    if s == K:
        cnt += 1
        return
    elif n == k:
        return
    elif s > K:
        return
    elif t+s < K:
        return
    else:
        f(n+1, k, s+num[n], t-num[n])
        f(n+1, k, s, t-num[n])



T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    num = list(range(1, N+1))
    cnt = 0
    cnt2 = 0
    f(0, N, 0, sum(num))
    print(cnt)