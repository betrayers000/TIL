import sys

sys.stdin = open('knap.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    table = [[0] * (K+1) for _ in range(N+1)]
    maxV = 0
    for i in range(1, N+1):
        v, c = map(int, input().split())
        for j in range(1, K+1):
            if v <= j:
                table[i][j] = max(table[i-1][j-v] + c, table[i-1][j])
            else:
                table[i][j] = table[i-1][j]
            if table[i][j] > maxV:
                maxV = table[i][j]
    print("#{} {}".format(t, maxV))

