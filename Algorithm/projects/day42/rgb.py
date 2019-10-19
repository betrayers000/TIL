import sys

sys.stdin = open('rgb.txt', 'r')

box = [[1, 2], [0, 2], [0, 1]]

N = int(input())
table = [[0] * 3 for _ in range(N)]
for i in range(N):
    info = list(map(int, input().split()))
    for j in range(3):
        if i == 0:
            table[i][j] = info[j]
        else:
            table[i][j] = min(table[i - 1][box[j][0]] + info[j], table[i - 1][box[j][1]] + info[j])
minV = table[-1][0]
# print(table)
# for i in range(N):
#     if table[-1][i] != 0:
#         minV = table[-1][i]
print(min(table[-1]))