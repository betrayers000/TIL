import sys

sys.stdin = open('birth.txt', 'r')


def f(n, k, d):
    if d == k:
        for t in temp:
            if t not in give and t != 1:
                give.append(t)
        return
    else:
        for i in range(len(table[n])):
            temp.append(table[n][i])
            f(table[n][i], k, d + 1)
            temp.pop()


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    table = [[]]
    for _ in range(N + 1):
        table += [[]].copy()
    for _ in range(M):
        a, b = map(int, input().split())
        table[a].append(b)
        table[b].append(a)
    give = []
    temp = []
    f(1, 2, 0)
    print("#{} {}".format(t, len(give)))
