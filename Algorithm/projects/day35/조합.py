import sys

sys.stdin = open('com.txt', 'r')

memo = {}

def f(n, u):
    # print(n, u)
    if u == 1:
        return n%1234567891
    else:
        if u %2:
            if memo.get((u//2)+1) != None:
                a = memo.get((u//2)+1)
            else:
                a = f(n, (u // 2) + 1)
                memo[(u // 2) + 1] = a
            if memo.get(u//2) != None:
                b = memo.get(u//2)
            else:
                b = f(n, u // 2)
                memo[u//2] = b
            return (a*b)%1234567891
        else:
            if memo.get(u//2) != None:
                a = memo.get(u//2)
            else:
                a = f(n, u//2)
                memo[u//2] = a
            return (a*a)%1234567891
        # if u % 2:
        #     return (f(n, (u // 2) + 1) * f(n, u // 2))%1234567891
        # else:
        #     return (f(n, u // 2) * f(n, u // 2))%1234567891
# def f(x, y):
#     xy = 1
#     while y > 0:
#         if (y % 2) == 1:
#             xy *= x
#             y -= 1
#             xy %= 1234567891
#         x *= x
#         x %= 1234567891
#         y /= 2
#     return xy

# def facto(n):
#     if n == 1:
#         return 1
#     else:
#         return facto(n-1) * n

T = int(input())
for t in range(1, T + 1):
    N, R = map(int, input().split())
    N_ = 1
    for i in range(N-R+1, N+1):
        N_ = N_ * i
        N_ %= 1234567891
    R_ = 1
    for j in range(1, R+1):
        R_ = R_ * j
        R_ %= 1234567891
    res = f(R_, 1234567891-2)
    # print(res, N_)
    # print(facto(4))
    print(f"#{t} {(N_*res)%1234567891}")
