import sys

sys.stdin = open('line.txt', 'r')


def find():
    q = [0] * (N + 1)
    front, rear = -1, -1
    for _ in range(N + 1):
        if _ != 0:
            if ind[_] == 0:
                rear += 1
                q[rear] = _
    while front != rear:
        front += 1
        n = q[front]
        res.append(str(n))
        for i in range(len(table[n])):
            v = table[n][i]
            ind[v] -= 1
            if ind[v] == 0:
                rear += 1
                q[rear] = v

res = []
N, M = map(int, input().split())
table = []
for _ in range(N + 1):
    table += [[]].copy()

ind = [0] * (N + 1)
for _ in range(M):
    s, e = map(int, input().split())
    table[s].append(e)
    ind[e] += 1
find()
print(' '.join(res))
