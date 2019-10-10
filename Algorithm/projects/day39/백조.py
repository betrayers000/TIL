import sys

sys.stdin = open('lake.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def mel(temp):
    for i in temp:
        x, y = i
        lake[x][y] = "."

def bfs(point):
    global R, C
    sx, sy = point[0]
    ex, ey = point[1]
    q = []
    # q.append([sx, sy])
    q.extend(point)
    lake[sx][sy] = "L"
    lake[ex][ey] = "R"
    temp = set()
    cnt = 0
    x1, y1 = 0, 0
    while 1:
        print(lake)
        while q:
            x1, y1 = q.pop(0)
            for i in range(4):
                nx, ny = x1 + dx[i], y1 + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if lake[nx][ny] == "R" and lake[x1][y1] == "L":
                        return cnt
                    elif lake[nx][ny] == "L" and lake[x1][y1] == "R":
                        return cnt
                    if lake[nx][ny] == ".":
                        q.append([nx, ny])
                        lake[nx][ny] = lake[x1][y1]
                    elif lake[nx][ny] == "X":
                        temp.add((nx, ny))
        mel(temp)
        temp = set()
        q.append([x1, y1])
        cnt += 1


R, C = map(int, input().split())
lake = []
point = []
for i in range(R):
    temp = list(input())
    lake.append(temp)
    for j in range(C):
        if lake[i][j] == 'L':
            point.append([i, j])
print(bfs(point))