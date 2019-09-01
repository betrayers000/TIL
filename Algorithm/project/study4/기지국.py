def cover(i, j, N)
    k = 0
    if station[i][j] =='A':
        k = 1
    if station[i][j] == 'B':
        k = 2
    if station[i][j] =='C':
        k = 3
    for h in range(1, k+1):
        if j+h < N: #오른쪽
            station[i][j+h] = 'X'
        if i+h < N : #아래
            station[i+h][j] = 'X'
        if j-h >= 0: #왼쪽
            station[i][j+h] = 'X'
        if i-h >= 0: #위
            station[i-h][j] = 'X'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    station = [list(input()) for x in range(N)]

    for i in range(N):
        for j in range(N):
           if  station[i][j]== 'A' or 'B' or 'C':
               cover(i, j, N)

    cnt = 0
    for i in range(N):
        for j in range(N):
            if station[i][j] =='H':
                cnt +=1
    print('#{} {}'.format(tc, cnt))
