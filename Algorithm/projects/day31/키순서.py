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

def check(n):
    s = []
    s.append(n)
    history = []
    while s:
        ns = s.pop()
        history.append(ns)
        for i in range(len(table[n])):
            a = table[n][i]
            if a not in history:
                s.append(a)
    print(history)

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    M = int(input())
    table = [[]]
    ind = [0] * (N + 1)
    rank = [0] * (N + 1)
    res = []
    for _ in range(N):
        table += [[]].copy()
    for _ in range(M):
        s, e = map(int, input().split())
        table[s].append(e)
        ind[e] += 1
    print(ind)
    p_sort()
    print(table)
    print(rank)
    print(res)
    for i in range(N):
        check(res[i])
