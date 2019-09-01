import sys

sys.stdin = open('block.txt', 'r')


def check(x, y, board):
    global N
    global M
    dx = [0, 1, -1]
    dy = [1, 0, 0]
    for z in range(3):
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 <= ny < M and N + 2 > nx >= 0:
            if board[nx][ny] == 0:
                return False
    return True


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    block = list(map(int, input().split()))
    M = max(block)
    board = [[0] * M] + [[0] * M for n in range(N)] + [[0] * M]
    for i in range(N):
        board[i + 1][:block[i]] = [1] * block[i]
    cnt = 0
    while 1:
        temp = []
        for i in range(1, N + 1):
            for j in range(M):
                if board[i][j] == 1:
                    if not check(i, j, board):
                        temp.append([i, j])
        if temp == []:
            break
        for z in temp:
            x, y = z
            board[x][y] = 0
        cnt += 1
    print(f"Case #{t}")
    print(cnt)
