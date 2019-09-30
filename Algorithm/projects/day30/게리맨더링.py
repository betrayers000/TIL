import sys

sys.stdin = open('gary.txt', 'r')

def get_sum(temp):
    total = 0
    for i in temp:
        total += hum[i]
    return total

def f(n, k,m, z):
    global minV
    if n == m:
        left = []
        for j in area:
            if j not in p:
                left.append(j)
        # print(left, p)
        # print(check(left), check(p))
        if check(left) and check(p):
            total = abs(get_sum(left) - get_sum(p))
            if minV > total:
                minV = total
        return
    else:
        for i in range(z, k):
            if used[i] == 0:
                used[i] = 1
                p[n] = area[i]
                f(n+1, k, m, i)
                used[i] = 0

def check(temp):
    global N
    stack = []
    stack.append(temp[0])
    visited = [0] * (N+1)
    while stack:
        n = stack.pop()
        visited[n] = 1
        for i in range(len(table[n])):
            m = table[n][i]
            if visited[m] == 0 and m in temp:
                stack.append(m)
    for i in range(len(temp)):
        if visited[temp[i]] == 0:
            return False
    return True

N = int(input())
hum = list(map(int, input().split()))
minV = 99999999
#인접리스트 만들기
table = [[]]
for _ in range(N+1):
    table += [[]].copy()
for _ in range(N):
    edge = list(map(int, input().split()))
    if edge[0] != 0:
        for i in range(1, len(edge)):
            table[_].append(edge[i]-1)
# 선거구 나누기
area = list(range(N))
for i in range(1, N//2 + 1):
    p = [0] * i
    used = [0] * N
    f(0, N, i, 0)
if minV == 99999999:
    minV = -1
print(minV)