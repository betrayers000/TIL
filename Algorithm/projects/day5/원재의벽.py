import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    N, A, B = map(int, input().split())
    result = []
    for R in range(1, N+1):
        C = int(N/R)
        Z = R-C
        if R-C < 0:
            Z = -Z
        r = (A*Z)+(B*(N-(R*C)))
        result.append(r)
    print(N, A, B, min(result))

