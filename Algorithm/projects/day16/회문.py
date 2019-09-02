import sys

sys.stdin = open('per.txt', 'r')

int(input())
for tc in range(3):
    N, M = map(int, input().split())
    cross = [list(input()) for _ in range(N)]

    wid = []
    col = []
    for i in range(len(cross)):
        col = []
        for j in range(N - M + 1):
            wid.append(cross[i][j:j + M])
            for c in range(j, j + M):
                col.append(cross[c][i])
            wid.append(col)

    for ii in range(len(wid)):
        if wid[ii][0:M + 1] == wid[ii][::-1]:
            print("#{} {}".format(tc + 1, ''.join(map(str, wid[ii]))))

# 1 JAEZNNZEAJ
# 2 MWOIVVIOWM
# 3 TLMMHOOOHMMLT
