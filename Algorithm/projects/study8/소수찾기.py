import sys

sys.stdin = open('find.txt', 'r')

def f(n, k, m):
    global cnt
    if n == m:
        num = ''.join(p)
        if int(num) > 1 and check(int(num)) and memo[int(num)]:
            cnt += 1
            print(num)
            memo[int(num)] = False
        return
    else:
        for i in range(k):
            if used[i] == 0:
                used[i] = 1
                p[n] = str(nums[i])
                f(n+1, k, m)
                used[i] = 0


def check(n):
    for i in range(2, n):
        if n%i == 0:
            return False
        if i**2 >= n:
            return True
    return True

T = int(input())
for t in range(1, T+1):
    cnt = 0
    memo = [True] * 1000000
    nums = list(map(int, list(input())))
    n = len(nums)
    for i in range(1, n+1):
        p = [0]*i
        used = [0] * n
        f(0, n, i)
    print(cnt)
