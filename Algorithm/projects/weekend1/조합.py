T = int(input())
for t in range(1, T+1):
    N, R = map(int, input().split())
    N_ = 1
    for i in range(N, N-R, -1):
        print(i)
        N_ = N_*i
    R_ = 1
    for j in range(R, 0, -1):
        print(j)
        R_ = R_ * j

    c = int(N_/R_)
    print(c%1234567891)