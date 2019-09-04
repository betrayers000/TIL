import sys

sys.stdin = open('2048.txt', 'r')


def move(C):
    global N
    if C == "up":
        for i in range(N - 1):
            for j in range(N):
                if sample_board[i][j] == 0:
                    z = 1
                    while i + z < N:
                        if board[i][j] == board[i+z][j]:
                            sample_board[i][j] = board[i + z][j] + board[i][j]
                            sample_board[i+z][j] = -1
                            break
                        else:
                            if board[i+z][j] != 0:
                                break
                        z += 1
    elif C == "down":
        for i in range(N-1, 0, -1):
            for j in range(N):
                if sample_board[i][j] == 0:
                    z = 1
                    while i - z >= 0:
                        if board[i][j] == board[i-z][j]:
                            sample_board[i][j] = board[i - z][j] + board[i][j]
                            sample_board[i-z][j] = -1
                            break
                        else:
                            if board[i-z][j] != 0:
                                break
                        z += 1

def clear(C):
    global N
    if C == "up":
        for i in range(N - 1):
            for j in range(N):
                z = 1
                while i + z < N:
                    if board[i][j] == 0 and board[i + z][j]:
                        board[i][j], board[i + z][j] = board[i + z][j], board[i][j]
                        break
                    z += 1
    elif C == "down":
        for i in range(N - 1, 0, -1):
            for j in range(N):
                z = 1
                while i - z >= 0:
                    if board[i][j] == 0 and board[i - z][j]:
                        board[i][j], board[i - z][j] = board[i - z][j], board[i][j]
                        break
                    z += 1
    return board


T = int(input())
for t in range(1, T + 1):
    N, C = input().split()
    N = int(N)
    board = [list(map(int, input().split())) for _ in range(N)]
    sample_board = [[0] * N for _ in range(N)]
    if C == "up" or C == "down":
        move(C)
        for i in range(N):
            for j in range(N):
                if sample_board[i][j] != 0:
                    if sample_board[i][j] == -1:
                        board[i][j] = 0
                    else:
                        board[i][j] = sample_board[i][j]
        clear(C)
    else:
        board = list(map(list, list(zip(*board))))
        if C == "left":
            C = "up"
        else:
            C = "down"
        move(C)
        for i in range(N):
            for j in range(N):
                if sample_board[i][j] != 0:
                    if sample_board[i][j] == -1:
                        board[i][j] = 0
                    else:
                        board[i][j] = sample_board[i][j]
        clear(C)
        board = list(map(list, list(zip(*board))))
    print(f"#{t}")
    for b in board:
        print(' '.join(map(str, board)))

