import sys

sys.stdin = open('board.txt', 'r')


def bfs(point):
    q = []
    q.append(point)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    result = []
    while 1:
        x, y, s = q.pop(0)
        if len(s) == 7:
            q.append([x, y, s])
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                q.append([nx, ny, s + board[x][y]])
                a = s + board[x][y]
                if len(a) == 7:
                    result.append(a)
    return set(result)


T = int(input())
for t in range(1, T + 1):
    board = [input().split() for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            result = result | bfs([i, j, ""])
    print(len(result))
