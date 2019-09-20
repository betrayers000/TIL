import sys

sys.stdin = open('cell.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def breed(cell):
    global point, temp, temp_point
    x, y, ori, n_ori = cell
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if point[nx][ny] == 0:
            # if [nx, ny] not in point:
            if [nx, ny, ori, ori] not in temp:
                temp.append([nx, ny, ori, ori])
                # temp_point.append([nx, ny])
            else:
                for t in temp:
                    if t[0] == nx and t[1] == ny:
                        if t[2] >= ori:
                            break
                        else:
                            temp.append([nx, ny, ori, ori])
                            # temp_point.append([nx, ny])
                            break
    return


T = int(input())
for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    cells = []
    point = [[0] * 3000 for _ in range(3000)]
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                cells.append([i, j, board[i][j], board[i][j]])
                # point.append([i, j])
                point[i][j] = 1
    time = 0
    while time < K:
        time += 1
        temp = []
        temp_point = []
        for i in range(len(cells)):
            cells[i][3] -= 1
            if cells[i][3] == -1:
                breed(cells[i])
            if cells[i][3] + cells[i][2] != 0:
                temp.append(cells[i])
        cells = temp
        for te in temp:
            point[te[0]][te[1]] = 1
        # print(time, len(cells))
    print(len(cells))
