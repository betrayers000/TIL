import sys

sys.stdin = open('lake.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = []
minV = 0

def enque(i, j):
    q.append([i, j])

<<<<<<< HEAD
=======
<<<<<<< HEAD
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

=======
# def enque(i, j, n):
#     if n == 1:
#         q.append([i, j])
#     else:
#         q2.append([i, j])
#
#
# def deque(n):
#     global minV, minV2
#     # print(q, minV, n, len(q))
#     if n == 1:
#         for i in range(len(q)):
#             x, y = q[i]
#             if visited[x][y] == minV and q[i] != [-1, -1]:
#                 q[i] = [-1, -1]
#                 return x, y, n
#         minV += 1
#         return deque(n)
#     else:
#         for i in range(len(q2)):
#             x, y = q2[i]
#             if visited[x][y] == minV2 and q2[i] != [-1, -1]:
#                 q2[i] = [-1, -1]
#                 return x, y, 2
#         minV2 += 1
#         return deque(2)
>>>>>>> 9ef1bad43f9f019499b622d78a06a92e555c9a42
>>>>>>> b6179c5bfdbbbb3f2365f6acc05cd3a646e9510b

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
<<<<<<< HEAD
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
=======
    while ice:
        # front += 1
        x, y = ice.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == 0 and lake[nx][ny] == "X":
                visited[nx][ny] = visited[x][y] + 1
                ice.append([nx, ny])
>>>>>>> 9ef1bad43f9f019499b622d78a06a92e555c9a42

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
<<<<<<< HEAD
maxV = 0
=======
<<<<<<< HEAD
=======
>>>>>>> b6179c5bfdbbbb3f2365f6acc05cd3a646e9510b
visited = [[0] * C for _ in range(R)]
>>>>>>> 9ef1bad43f9f019499b622d78a06a92e555c9a42
for i in range(R):
    temp = list(input())
    lake.append(temp)
    for j in range(C):
        if lake[i][j] == 'L':
            point.append([i, j])
<<<<<<< HEAD
        elif lake[i][j] == "X":
            ice.append([i, j])
print(bfs(point))
=======
        if lake[i][j] == "." or lake[i][j] == "L":
            ice.append([i, j])
water(ice)
<<<<<<< HEAD
enque(point[0][0], point[0][1])
swan()
# print(point)
print(maxV)
=======
# 이분탐색으로 bfs 돌려야함 ?
>>>>>>> 9ef1bad43f9f019499b622d78a06a92e555c9a42
>>>>>>> b6179c5bfdbbbb3f2365f6acc05cd3a646e9510b
