import sys

sys.stdin = open('input.txt', 'r')


T = int(input())
nums = list(range(10))
for t in range(1, T + 1):
    N = int(input())
    a = 10 ** N - 10 ** (N - 1)
    b = 1
    for i in range(10, 10-N, -1):
        b *= i
    c = 1
    for i in range(9, 9-N+1, -1):
        c *= i
    res = (b-c)/a
    res = round(res, 5)
    print("#%d %0.5f" %(t, res))
