N = 4
edge = [2, 3, 4, 5, 4, 6, 7, 6]
M, K = 3, 6

def find(n):
    global p
    if n == p[n]:
        return n
    else:
        return find(p[n])

def rep(n):
    while p[n] != n:
        n = p[n]
    return n

p = list(range(8))
for i in range(N):
    a, b = edge[i * 2], edge[i * 2 + 1]
    p[find(b)] = find(a)
temp = 0
cnt = 0
for j in p:
    if j != 0:
        if temp != find(j):
            cnt += 1
            temp = find(j)
res = 0
if find(p[M]) == find(p[K]):
    res = 1
print(cnt, res)

