def check(x1, y1, x2, y2, c):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if board[i][j] > c:
                return False
    return True

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    board = [[0]*M for x in range(N)]
    for a in range(K):
        x1, y1, x2, y2, c = map(int, input().split())
        # result = 0
        # # 해당영역이 칠해졌을때....?
        # for i in range(x1, x2+1):
        #     for j in range(y1, y2+1):
        #         if board[i][j] > c:
        #             result = 1
    # 해당영역이 칠해지지 않았다면
    #     if result ==0:
        if check(x1, y1, x2, y2, c):
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    board[i][j] = c


    bright = [0] * 11
    for i in range(N):
        for j in range(M):
            bright[board[i][j]] +=1


    print('#{} {}'.format(tc, max(bright)))