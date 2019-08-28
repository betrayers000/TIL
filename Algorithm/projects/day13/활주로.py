import sys

sys.stdin = open('sky.txt', 'r')

def get_cnt(board, N):
    global X
    cnt = 0
    sample = [[0]* N for _ in range(N)]
    for i in range(N):
        for j in range(N-1):
            if board[i][j] > board[i][j+1]:
                if board[i][j] - board[i][j+1] > 1:
                    break
                total = 0
                ans = board[i][j+1] * X
                for x in range(X):
                    if j+1+x >= N:
                        break
                    if sample[i][j+1+x] != 0:
                        break
                    total += board[i][j+1+x]
                    sample[i][j+1+x] = 1
                if total != ans:
                    break
            if board[i][j] < board[i][j+1]:
                if board[i][j+1] - board[i][j] > 1:
                    break
                total = 0
                ans = board[i][j] * X
                for x in range(X):
                    if j-x < 0:
                        break
                    if sample[i][j-x] != 0:
                        break
                    total += board[i][j-x]
                    sample[i][j-x] = 1
                if total != ans:
                    break
        else:
            cnt+= 1
    return cnt

T = int(input())
for t in range(1, T+1):
    N, X = map(int, input().split())
    board_ = [list(map(int, input().split())) for n in range(N)]
    board_h = list(map(list, zip(*board_)))
    result = get_cnt(board_.copy(), N) + get_cnt(board_h.copy(), N)
    print(result)

