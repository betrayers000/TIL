di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
T =int(input())
for tc in range(1, T+1):
    N = int(input())
    snail = [[0] * N for x in range(N)]
    # N_origin = N
    print('#{}'.format(tc))
    i = 0 #시작위치설정
    j = 0
    k = 1 # 시작 값
    dir = 0 # 방향
    while k <= N * N:
        snail[i][j] = k
        k += 1
        ni = i + di[dir]
        nj = j + dj[dir]
        if ni>=0 and ni< N and nj>=0 and nj<N and snail[ni][nj]==0: #배열안에 있고 칸이 0이면
            # 새로운 위치
            i, j = ni, nj
            snail[i][j] = k # 1씩증가
        else:
            dir = (dir+1) % 4
            i += di[dir]#벗어나면 다시 돌아와야함
            j += dj[dir]
    print(snail)

    # N -=1
    # while N> 0:
    #     for a in range(4): # 4방향
    #         for b in range(N): # N-1씩 이동
    #             snail[i][j] = k
    #             k+=1
    #             i += di[a]
    #             j += dj[a]




    # print('{}'.format(snail))








