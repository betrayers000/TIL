import sys

sys.stdin = open('sticky.txt', 'r')


def get_area(temp):
    global H, W
    for i in range(4):
        h1, w1 = info[temp[0]]
        h2, w2 = info[temp[1]]
        if i == 1:
            h1, w1 = w1, h1
        elif i == 2:
            h2, w2 = w2, h2
        elif i == 3:
            h1, w1 = w1, h1
            h2, w2 = w2, h2
        th1, tw1 = w1 + w2, max(h1, h2)
        th2, tw2 = max(w1, w2), h1 + h2
        if (th1 <= H and tw1 <= W) or (th2 <= H and tw2 <= W):
            return True
    return False


def get_sum(temp):
    ax, ay = info[temp[0]]
    bx, by = info[temp[1]]
    return (ax * ay) + (bx * by)


def f(n, k, m, z):
    global H, W, maxV
    if n == m:
        if get_area(p):
            res = get_sum(p)
            if maxV < res:
                maxV = res
        return
    else:
        for i in range(z, k):
            if used[i] == 0:
                used[i] = 1
                p[n] = i
                f(n + 1, k, m, i)
                used[i] = 0


H, W = map(int, input().split())
N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
maxV = 0
n = len(info)
used = [0] * n
p = [0] * 2
f(0, n, 2, 0)
print(maxV)
