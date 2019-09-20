def bfs(n, M):
    q = [0] * 1000000
    front, rear = -1, -1
    rear += 1
    q[rear] = n
    visited[n] = 1
    while front != rear:
        front += 1
        calc = [q[front] +1,q[front] -1, q[front]*2, q[front] -10]
        for i in range(4):
            num = calc[i]
            if 1<= num<= 1000000 and visited[num] == 0:
                visited[num] = visited[q[front]] + 1
                rear += 1
                q[rear] = num
                if num == M:
                    return visited[num]-1
    return 0


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    print("#{} {}".format(t, bfs(N, M)))
