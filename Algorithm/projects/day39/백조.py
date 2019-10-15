import sys

sys.stdin = open('lake.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = []
minV = 0

def enque(i, j):
    q.append([i, j])


def deque():
    global minV
    # print(q, minV, n, len(q))
    for i in range(len(q)):
        x, y = q[i]
        if visited[x][y] == minV and q[i] != [-1, -1]:
            q[i] = [-1, -1]
            minV = 0
            return x, y
    minV += 1
    return deque()


def water(ice):
    global R, C
    while ice:
        # front += 1
        x, y = ice.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == 0 and lake[nx][ny] == "X":
                visited[nx][ny] = visited[x][y] + 1
                ice.append([nx, ny])

def swan():
    global R, C, maxV
    while 1:
        x, y = deque()
        # print(visited[x][y], x, y)
        if visited[x][y] > maxV:
            maxV = visited[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx == point[1][0] and ny == point[1][1]:
                return
            if 0 <= nx < R and 0<= ny < C and lake[nx][ny] != "L":
                enque(nx, ny)
                lake[nx][ny] = "L"

R, C = map(int, input().split())
lake = []
point = []
ice = []
maxV = 0
visited = [[0] * C for _ in range(R)]
for i in range(R):
    temp = list(input())
    lake.append(temp)
    for j in range(C):
        if lake[i][j] == 'L':
            point.append([i, j])
        if lake[i][j] == "." or lake[i][j] == "L":
            ice.append([i, j])
water(ice)
enque(point[0][0], point[0][1])
swan()
# print(point)
print(maxV)