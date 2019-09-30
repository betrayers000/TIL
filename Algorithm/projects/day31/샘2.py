import sys

sys.stdin = open('sam.txt', 'r')

for t in range(1, 11):
    input()
    N = 100
    board = [list(map(int, input().split())) for _ in range(N)]
    minV = 9999999
    mindex = 0
    # for h in range(1, 30):
    #     temp = 0
    #     temp_ = 0
    #     for i in range(N):
    #         temp = 0
    #         for n in board[i]:
    #             temp += abs(n - h)
    #         if minV > temp:
    #             minV = temp
    #             mindex = h
    #         temp = 0
    #         for j in range(N):
    #             temp += abs(board[j][i] -h)
    #         if minV > temp:
    #             minV = temp
    #             mindex = h
    #         temp += abs(board[i][i] - h)
    #         temp_ += abs(board[i][N-i-1] - h)
    #     if minV > min(temp, temp_):
    #         minV = min(temp, temp_)
    #         mindex = h
    # print(minV, mindex)

    for h in range(1, 30):
        temp = 0
        temp_ = 0
        for i in range(N):
            val = 0
            val2 = 0
            temp += abs(board[i][i] - h)
            temp_ += abs(board[i][N - i - 1] - h)
            for j in range(N):
                val += abs(board[i][j] - h)
                val2 += abs(board[j][i] - h)
            if minV > min(val, val2):
                minV = min(val, val2)
                mindex = h
        if minV > min(temp, temp_):
            minV = min(temp, temp_)
            mindex = h
    print(minV, mindex)