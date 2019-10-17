import sys

sys.stdin = open('sticky.txt', 'r')


def get_area():
    global H, W
    h1, w1 = info[p[0]]
    h2, w2 = info[p[1]]




def f(n, k, m, z):
    global H, W, maxV
    if n == m:
        print(p)
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
