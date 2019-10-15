import sys

sys.stdin = open('lake.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def mel():
    global R, C
    temp = []
    ice_temp = []
    for i in ice:
        x, y = i
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < R and 0 <= ny < C:
                if lake[nx][ny] == "." or lake[nx][ny] == "L":
                    temp.append([x, y])
                    break
        else:
            ice_temp.append([x, y])
    for i in temp:
        x, y = i
        lake[x][y] = "."
    return ice_temp


def bfs(point):
    global R, C
    sx, sy = point[0]
    ex, ey = point[1]
    q = []
    q.append([sx, sy])
    lake[sx][sy] = "L"
    temp = set()
    cnt = 0
    while 1:
        while q:
            x1, y1 = q.pop(0)
            for i in range(4):
                nx, ny = x1 + dx[i], y1 + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if nx == ex and ny == ey:
                        return cnt
                    # if lake[nx][ny] == "R" and lake[x1][y1] == "L":
                    #     return cnt
                    # elif lake[nx][ny] == "L" and lake[x1][y1] == "R":
                    #     return cnt
                    if lake[nx][ny] == ".":
                        q.append([nx, ny])
                        lake[nx][ny] = 'L'
                    elif lake[nx][ny] == "X":
                        temp.add((nx, ny))
        ice = mel()
        q = list(temp)
        temp = set()
        cnt += 1


R, C = map(int, input().split())
lake = []
point = []
ice = []
for i in range(R):
    temp = list(input())
    lake.append(temp)
    for j in range(C):
        if lake[i][j] == 'L':
            point.append([i, j])
        elif lake[i][j] == "X":
            ice.append([i, j])
print(bfs(point))
