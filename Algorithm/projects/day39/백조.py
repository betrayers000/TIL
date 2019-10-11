import sys

sys.stdin = open('lake.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


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


R, C = map(int, input().split())
lake = []
point = []
ice = []
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
# 이분탐색으로 bfs 돌려야함 ?