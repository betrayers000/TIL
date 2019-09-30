import sys

sys.stdin = open('work.txt', 'r')

def find():
    q = [0] * (V+1)
    front, rear = -1, -1
    for i in range(len(ind)):
        if i != 0:
            if ind[i] == 0:
                rear += 1
                q[rear] = i
    while front != rear:
        front += 1
        n = q[front]
        visited[n] = 1
        res.append(str(n))
        for i in range(len(table[n])):
            v = table[n][i]
            ind[v] -= 1
            if ind[v] == 0:
                rear += 1
                q[rear] = v



for t in range(1, 11):
    V, E = map(int, input().split())
    table = [[]]
    ind = [0] * (V+1)
    visited = [0] * (V+1)
    for _ in range(V):
        table += [[]].copy()
    edge = list(map(int, input().split()))
    res = []
    for i in range(E):
        s, e = edge[i*2], edge[i*2+1]
        table[s].append(e)
        ind[e] += 1
    find()
    print("#{} {}".format(t, ' '.join(res)))