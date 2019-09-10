import sys

sys.stdin = open('hanaload.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    table = [[0] * (N+1) for _ in range(N+1)]
    temp = []
    mst = [0] * (N+1)
    E = 0
    while 1:
        b = input().split()
        if len(b) == 1:
            E = float(b[0])
            break
        else:
            temp.extend(list(map(int, b)))
    land = [[0]]
    for i in range(len(temp)//2):
        land.append([temp[i], temp[i+len(temp)//2]])


    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if land[i][0] == land[j][0] or land[i][1] == land[j][1]:
                a = (abs(land[i][0] - land[j][0]) + abs(land[j][1] - land[i][1]))**2
            else:
                a = (abs(land[i][0] - land[j][0])**2 + abs(land[j][1] - land[i][1])**2)
            table[i][j] = table[j][i] = E * a

    mst[1] = 1
    total = 0
    while 1:
        minV = max(table[1])*2
        minidx = -1
        for i in range(N+1):
            if mst[i] == 1:
                for j in range(1, N+1):
                    if mst[j] != 1 and table[i][j] != 0:
                        if minV > table[i][j]:
                            minV = table[i][j]
                            minidx = j
        if minidx != -1:
            total += minV
            mst[minidx] = 1
        else:
            break
    print(int(total))


