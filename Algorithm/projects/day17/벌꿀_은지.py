import sys

sys.stdin = open('honey.txt', 'r')

def func(s, k):
    global n, m, c, check, split_arr, p, maxV
    if s == k and sum(p) <= c:
        maxV = max(maxV, sum(list(map(lambda x: x*x, p))))
        print(p)
    elif s < k:
        for i in range(m):
            if not check[i]:
                if split_arr.count(split_arr[i]) == p.count(split_arr[i]):
                    continue
                p[s] = split_arr[i]
                check[i] = True
                func(s+1, k)
                check[i] = False
int(input())
for t in range(1):
    n, m, c = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = []
    for i in range(n):
        maxV = 0
        for j in range(n-m+1):
            split_arr = arr[i][j:j + m]
            for k in range(1, m+1):
                check = [False] * m
                p = [0] * k
                func(0, k)
        res.append(maxV)
    print('#{} {}'.format(t+1, sum(sorted(res, reverse=True)[:2])))