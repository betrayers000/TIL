import sys

sys.stdin = open('long.txt', 'r')


def p_sort():
    global cnt
    q = [0] * (M + 1)
    front, rear = -1, -1
    for i in range(1, len(ind)):
        if ind[i] == 0:
            rear += 1
            q[rear] = i
            rank[i] = 1
            count[rank[i]] += 1
    while front != rear:
        front += 1
        n = q[front]
        res.append(n)
        for i in range(len(table[n])):
            a = table[n][i]
            ind[a] -= 1
            if ind[a] == 0:
                rear += 1
                q[rear] = a
                rank[a] = rank[n] + 1
                count[rank[a]] += 1


def check(n, z):
    global visited, N
    s = []
    s.append(n)
    cnt = 0
    while s:
        ns = s.pop()
        visited[ns] = 1
        if ns != n:
            cnt += 1
        for i in range(len(table[ns])):
            a = table[ns][i]
            if visited[a] == 0:
                s.append(a)
    # if z == N - cnt - 1:
    #     for i in range(z, len(res)):
    #         if visited[res[i]] == 0:
    #             return False
    #     return True
    # return False


def check_re(n, z):
    global temp, visited
    s = []
    s.append(n)
    cnt = 0
    while s:
        ns = s.pop()
        visited[ns] = 1
        if ns != n:
            cnt += 1
        # temp.append(ns)
        for i in range(len(table_[ns])):
            a = table_[ns][i]
            # if a not in temp:
            if visited[a] == 0:
                s.append(a)
    # if z == cnt:
    #     for i in range(z):
    #         if visited[res[i]] == 0:
    #             return False
    #     return True
    # return False


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    M = int(input())
    table = [[]]
    table_ = [[]]
    ind = [0] * (N + 1)
    rank = [0] * (N +1)
    count = [0] * (N + 1)
    res = []
    for _ in range(N):
        table += [[]].copy()
        table_ += [[]].copy()
    for _ in range(M):
        s, e = map(int, input().split())
        table[s].append(e)
        table_[e].append(s)
        ind[e] += 1
    p_sort()
    cnt = 0
    print(count)
    print(res)
    print(rank)
    for i in range(len(res)):
        # print(i, rank.index(i))
        visited = [0] * (N + 1)
        check(res[i], i)
        check_re(res[i], i)
        # if check(res[i], i) and check_re(res[i], i):
        #     pass
        # print(temp, visited)
        if sum(visited) == N:
            cnt += 1
    print("#{} {}".format(t, cnt))
