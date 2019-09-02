import sys

sys.stdin = open('input.txt')


def change_board(x, y, nx, ny):
    for i in range(x, nx + 1):
        for j in range(y, ny + 1):
            board[i][j] = 0
    result.append([nx - x + 1, ny - y + 1])


T = int(input())
for t in range(1, 2):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            ni, nj = i, j
            if board[i][j] != 0:
                while 1:
                    nj += 1
                    if 0 <= nj < N:
                        if board[i][nj] == 0:
                            nj = nj - 1
                            break
                    else:
                        nj = nj - 1
                        break
                while 1:
                    ni += 1
                    if 0 <= ni < N:
                        if board[ni][nj] == 0:
                            ni = ni - 1
                            break
                    else:
                        ni = ni - 1
                        break
                change_board(i, j, ni, nj)
    result = sorted(sorted(result, key=lambda x: x[0]), key=lambda x: x[0]*x[1])
    p = [len(result)]
    for r in result:
        p.extend(r)
    print(f"#{t} {' '.join(map(str, p))}")

