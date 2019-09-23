import sys

sys.stdin = open('mst.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    edge = sorted(edge, key=lambda x: x[2])
    total = 0
    # 인접행렬 구하기
    table = [[0] * (N+1) for _ in range(N+1)]
    for eg in edge:
        n1, n2, w = eg
        table[n1][n2] = w
        table[n2][n1] = w
    mst = [0] * (N+1)
    mst[0] = 1
    while 1:
        if sum(mst) == N+1:
            break
        idx = 0
        minV = 9999
        for i in range(len(mst)):
            if mst[i] == 1:
                for j in range(N+1):
                    if table[i][j] != 0 and mst[j] == 0:
                        if minV > table[i][j]:
                            minV = table[i][j]
                            idx = j

        total += minV
        mst[idx] = 1
    print("#{} {}".format(t, total))
