import sys

sys.stdin = open('com.txt', 'r')

def f(n, u):
    # print(n, u)
    if u == 1:
        return n
    else:
        if u % 2:
            return f(n, (u//2)+1) * f(n, u//2)
        else:
            return f(n, u//2) * f(n, u//2)

T = int(input())
for t in range(1, T+1):
    N, R = map(int, input().split())
    N_ = 1
    for i in range(N, N-R, -1):
        N_ = N_*i
    R_ = 1
    for j in range(R, 0, -1):
        R_ = R_ * j
    print(f(R_, 9))
    print(f"#{t} {result}")
