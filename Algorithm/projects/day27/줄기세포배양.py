import sys

sys.stdin = open('cell.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def breed(cell, t, ori):
    global point, temp, temp_point
    x, y = cell
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 750 and 0<= ny < 750:
            if point[nx][ny] == 0:
                cells[(nx, ny)] = (ori, ori)
                point[nx][ny] = t
            elif point[nx][ny] == t:
                a, b = cells[(nx, ny)]
                if b < ori:
                    cells[(nx, ny)] = (a, ori)
    return


T = int(input())
for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    cells = {}
    point = [[0] * 750 for _ in range(750)]
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                cells[(i+K, j+K)] = (board[i][j], board[i][j])
                point[i+K][j+K] = 1
    time = 0
    while time < K:
        time += 1
        temp = []
        for i in list(cells.keys()):
            a, b = cells[i]
            a -= 1
            cells[i] = (a, b)
            if a == -1:
                breed(i, time, b)
            if b + a == 0:
                temp.append(i)
        for i in temp:
            del cells[i]
    # print(cells)
    print(len(cells))
