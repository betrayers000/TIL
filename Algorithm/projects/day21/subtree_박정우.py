import sys

sys.stdin = open('subtree.txt', 'r')


def f(n):
    global cnt
    if n > 0:
        cnt += 1
        f(ch1[n])
        f(ch2[n])

T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    e = list(map(int, input().split()))
    ch1 = [0] * (E+2)
    ch2 = [0] * (E+2)
    for i in range(1, E*2, 2):
        if ch1[e[i-1]] == 0:
            ch1[e[i-1]] = e[i]
        else:
            ch2[e[i-1]] = e[i]
    cnt = 0
    f(N)
    print(cnt)
