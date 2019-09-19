import sys

sys.stdin = open('cell.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def breed(cell):
    global point
    x, y, ori, temp_ori = cell
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if point[nx][ny]:
            if check(nx, ny, ori):
                temp.append([nx, ny, ori, ori])
                point[nx][ny] = False

def check(x, y, ori):
    global temp
    for t in temp:
        if t[0] == x and t[1] == y:
            if ori > t[3]:
                temp.remove(t)
                return True
            else:
                return False
    return True

T = int(input())
for t in range(1, 2):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    cells = []
    point = [[True] * 3000 for _ in range(3000)]
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                cells.append([i, j, board[i][j], board[i][j]])
                point[i][j] = False
    time = 0
    while time < K:
        time += 1
        temp = []
        for i in range(len(cells)):
            cells[i][3] -= 1
            if cells[i][3] == -1:
                breed(cells[i])
            if cells[i][3] + cells[i][2] == 0:
                continue
            temp.append(cells[i])
        cells = temp
        print(len(cells), cells)
    print(len(cells))
