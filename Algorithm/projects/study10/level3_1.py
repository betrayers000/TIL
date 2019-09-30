import sys

sys.setrecursionlimit(10**6)
memo = [0] * 2001
memo[1] = 1
memo[2] = 2

def f(n):
    if memo[n] != 0:
        return memo[n]
    else:
        memo[n] = f(n-2) + f(n-1)
    return memo[n]

def solution(n):
    answer = 0
    return answer


f(2000)
print(memo[500])