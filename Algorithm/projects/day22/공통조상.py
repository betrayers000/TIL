import sys

sys.stdin = open('ancestor.txt', 'r')

def get_ancestor(n):
    temp = []
    last = par[n]
    while last != 0:
        temp.append(last)
        last = par[last]
    return temp

def f(n):
    global cnt
    if n > 0:
        cnt += 1
        f(ch1[n])
        f(ch2[n])


T = int(input())
for t in range(1, T+1):
    V, E, T1, T2 = map(int, input().split())
    e = list(map(int, input().split()))
    cnt = 0
    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)
    par = [0] * (V+1)
    for i in range(1, E*2, 2):
        if ch1[e[i-1]] == 0:
            ch1[e[i-1]] = e[i]
        else:
            ch2[e[i-1]] = e[i]
        par[e[i]] = e[i-1]
    a1 = get_ancestor(T1)
    a2 = get_ancestor(T2)
    result = []
    while a1:
        z = a1.pop()
        if z in a2:
            result.append(z)
    f(result[-1])
    print(result[-1], cnt)
