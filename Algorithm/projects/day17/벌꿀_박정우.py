import sys

sys.stdin = open('honey.txt', 'r')

def f(n, k, m, p, used, select, s):
    global K, max_
    if sum(p) > K:
        return
    elif n == m:
        if max_ < s:
            max_ = s
        return
    else:
        for i in range(k):
            if used[i] == 0:
                if select.count(select[i]) == p.count(select[i]):
                    continue
                p[n] = select[i]
                f(n + 1, k, m, p, used, select, s + (select[i] ** 2))
                used[n] = 0

def check(i, N, M, K):
    for j in range(N - M + 1):
        select = board[i][j:j + M]
        n = len(select)
        used = [0] * n
        for s in range(1, n + 1):
            p = [0] * s
            f(0, n, s, p, used, select, 0)

T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    temp = []
    for i in range(N):
        max_ = 0
        check(i, N, M, K)
        temp.append(max_)
    print(sum(sorted(temp)[-2:]))
