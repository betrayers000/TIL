import sys

sys.stdin = open('group.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    h = list(map(int, input().split()))
    check = list(range(N+1))
    path = []
    for i in range(0, len(h), 2):
        path.append([h[i], h[i + 1]])
    stack = []
    stack.append(check[1])
    check[1] = 0
    his = []
    cnt = 1
    while stack:
        now = stack.pop()
        for p in path:
            if p[0] == now and p[1] not in his:
                his.append(p[1])
                stack.append(p[1])
                check[p[1]] = 0
            elif p[1] == now and p[0] not in his:
                his.append(p[0])
                stack.append(p[0])
                check[p[0]] = 0
        if stack == []:
            for i in range(len(check)):
                if check[i] != 0:
                    stack.append(check[i])
                    check[i] = 0
                    cnt += 1
                    break
    print("#{} {}".format(t, cnt))




