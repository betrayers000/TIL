import sys

sys.stdin = open('tri.txt', 'r')

N = int(input())
table = [[0] * N for _ in range(N)]
for i in range(N):
    info = list(map(int, input().split()))
    for j in range(len(info)):
        if i == 0:
            table[i][j] = info[i]
        else:
            table[i][j] = max(table[i-1][j-1]+info[j], table[i-1][j]+info[j])
print(max(table[-1]))