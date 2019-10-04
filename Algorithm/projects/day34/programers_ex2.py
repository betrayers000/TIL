N = 5
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
K = 3


def f(n, d, table):
    for i in range(len(table[n])):
        e, w = table[n][i]
        d[e] = min(d[e], d[n] + w)

def solution(N, road, K):
    answer = 0
    table = [[]]
    d = [20000] * (N+1)
    visited = [0] * (N+1)
    visited[0] = 1
    for _ in range(N):
        table += [[]].copy()
    for r in road:
        s, e, w = r
        table[s].append([e, w])
        table[e].append([s, w])
    print(table)
    d[1] = 0
    while 1:
        minV = 99999
        minidx = 0
        for i in range(N+1):
            if d[i] != 20000 and visited[i] == 0:
                if minV > d[i]:
                    minV = d[i]
                    minidx = i
        f(minidx, d, table)
        visited[minidx] = 1
        if sum(visited) == N+1:
             break
    for i in range(1, N+1):
        if d[i] <= K:
            answer += 1
    return answer

print(solution(N, road, K))
