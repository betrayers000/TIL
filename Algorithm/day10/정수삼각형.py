import sys

sys.stdin = open('input.txt', 'r')

def tri_sum(n, k, used, temp):
    if n == k:
        print(temp)
        return
    else:
        for i in range(k):
            if i <= k:
                if used[i] == 0:
                    used[i] = 1
                    temp[i] = tri[n][i]
                    tri_sum(n+1, k, used, temp)
                    used[n] = 0
                    temp[n] = 0



N = int(input())
temp = [0] * N
used = [0] * N
result = []
tri = [list(map(int, input().split())) for n in range(N)]
tri_sum(0, N, used, temp)
total = 0

