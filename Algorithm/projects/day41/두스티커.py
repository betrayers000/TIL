import sys

sys.stdin = open('sticky.txt', 'r')

def turn(temp):
    return [temp[1], temp[0]]

def harp(temp, d):
    if d == "h":
        return [temp[0]//2, temp[1]]
    else:
        return [temp[0], temp[1]//2]

def stick(p):
    global H, W
    a = info[p[0]]
    b = info[p[1]]

def f(n, k, m, z):
    if n == m:
        stick(p)
        return
    else:
        for i in range(z, k):
            if used[i] == 0:
                used[i] = 1
                p[n] = i
                f(n+1, k, m, i)
                used[i] = 0

H, W = map(int, input().split())
N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
board = [[0] * W for _ in range(H)]
n = len(info)
used = [0] * n
p = [0] * 2
f(0, n, 2, 0)
