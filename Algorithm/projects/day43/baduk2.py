
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
deq = []
group = 3
group_info = []
for i in range(N):
    for j in range(M):
        if data[i][j] == 2:
            data[i][j] = group
            deq.append((i, j))
            group_info.append([1, set({})])
            while len(deq):
                x, y = deq.pop()
                for d in dxy:
                    nx, ny = x + d[0], y + d[1]
                    if 0 <= nx < N and 0 <= ny < M:
                        if data[nx][ny] == 2:
                            data[nx][ny] = group
                            group_info[-1][0] += 1
                            deq.append((nx, ny))
                        elif data[nx][ny] == 0:
                            group_info[-1][1].add((nx, ny))
            if len(group_info[-1][1]) > 2:
                group_info.pop()
            group += 1
result = 0
n = len(group_info)
deq.append((0, [False for _ in range(len(group_info))], set({})))
while len(deq):
    k, pick, sum_blank = deq.pop()
    if k == n:
        cnt = 0
        for i in range(n):
            if pick[i]:
                cnt += group_info[i][0]
        result = max(result, cnt)
    else:
        pick[k] = False
        deq.append((k + 1, pick[:], sum_blank))
        if len(sum_blank | group_info[k][1]) <= 2:
            pick[k] = True
            deq.append((k + 1, pick, sum_blank | group_info[k][1]))
print(result)