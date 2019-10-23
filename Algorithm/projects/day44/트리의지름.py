import sys

sys.stdin = open('tree.txt', 'r')


def f(n):
    q = [0] * 100001
    front, rear = -1, -1
    rear += 1
    q[rear] = n
    visited[n] = 1
    maxV = 0
    idx = 0
    while front != rear:
        front += 1
        v = q[front]
        for i in range(len(table[v])):
            nv, w = table[v][i]
            if visited[nv] == 0:
                rear += 1
                q[rear] = nv
                visited[nv] = visited[v] + w
                if maxV < visited[nv]:
                    maxV = visited[nv]-1
                    idx = nv
    return maxV, idx


V = int(input())
table = [[]]
for _ in range(V):
    table += [[]].copy()
for _ in range(V):
    inplist = list(map(int, input().split()))
    for i in range(1, len(inplist) - 1, 2):
        table[inplist[0]].append([inplist[i], inplist[i + 1]])
res = 0
start = 1
for i in range(2):
    visited = [0] * (V + 1)
    temp, start = f(start)
    res = temp
print(res)
