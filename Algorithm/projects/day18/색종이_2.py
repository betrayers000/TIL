import sys

sys.stdin = open('paper.txt', 'r')

board = [list(map(int, input().split())) for _ in range(3)]
size = [0, 5, 5, 5, 5, 5]


def check(i, j, k):
    result = False
    for x in range(k):
        if result:
            break
        for y in range(k):
            if 0 <= i + x < 3 and 0 <= i + y < 3:
                if board[i + x][j + y] == 0:
                    result = True
                    break
    return not result


for i in range(3):
    for j in range(3):
        if board[i][j] == 1:
            for k in range(1, 6):
                if check(i, j, k):
                    break
