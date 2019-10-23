import sys

sys.stdin = open('tree.txt', 'r')


def f(n, k, s):
    global maxV
    if n == k:
        if maxV < s:
            maxV = s
        return
    else:
        for i in range(len(table[n])):
            nn, w =table[n][i]
            if visited[nn] == 0:
                visited[nn] = 1
                f(nn, k, s+w)
                visited[nn] = 0


V = int(input())
visited = [0] * (V+1)
table = [[]]
for _ in range(V):
    table += [[]].copy()
for _ in range(V):
    inplist = list(map(int, input().split()))
    for i in range(1, len(inplist) - 1, 2):
        table[inplist[0]].append([inplist[i], inplist[i + 1]])
maxV = 0
root = []
for i in range(len(table)):
    if len(table[i]) == 1:
        root.append(i)
# print(root)
for i in range(len(root)):
    for j in range(i+1, len(root)):
        f(root[i], root[j], 0)
print(maxV)