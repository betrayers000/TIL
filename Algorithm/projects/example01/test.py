import sys

sys.stdin = open('input.txt', 'r')

def check(x1, y1, x2, y2, c):
    check = True
    for i in range(x1, x2+1):
        if not check:
            break
        for j in range(y1, y2+1):
            if board[i][j] > c:
                check = False
                break
    return check

T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    c_list = [0] * 11
    for k in range(K):
        x1, y1, x2, y2, c = map(int, input().split())
        if check(x1, y1, x2, y2, c):
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    board[i][j] = c
    for i in range(N):
        for j in range(M):
            c_list[board[i][j]] += 1
    print("#{} {}".format(t, max(c_list)))