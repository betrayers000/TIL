import sys

sys.stdin = open('process.txt', 'r')


def dfs():
    pass

# def make_line(point, dir):
#     if dir == 1:
#
#     elif dir == 2:
#
#     elif dir == 3:
#
#     elif dir == 4:


T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = []
    board.append([2] * N)
    for n in range(N):
        board.append([2] + list(map(int, input().split())) + [2])
    board.append([2] * N)

    core = []
    for i in range(N):
        for j in range(N):
            if i != 0 and j != 0:
                if board[i][j] == 1:
                    core.append([i, j])
    print(core)





