def bfs(i, j, N):
    global maze
    q = [] # 큐생성
    visited = [[]*N for _ in range(N)] # visited 생성
    q.append([i, j]) # 시작점 인큐
    visited[i][j] = 1 # 시작점 방문표시
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    #탐색
    while(len(q) != 0):
        i, j = q.pop(0)
        if maze[i][j] == "3":
            return visited[i][j] - 2
        else:
            for k in range(4):
                x = i + di[k]
                y = j + dj[k]
                if 0 <= x < N and 0 <= x < N:
                    if maze[x][y] != "1" and visited[x][y] == 0:
                        q.append([x, y])
                        visited[x][y] = visited[i][j] + 1
    return 0




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    startI = 0
    startJ = 0
    bfs(startI, startJ, N)