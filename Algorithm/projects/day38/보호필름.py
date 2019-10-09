import sys

sys.stdin = open('protect.txt', 'r')

def check(temp):
    global W, D, K
    cnt = 0
    for i in range(W):
        t = temp[0][i]
        for j in range(D):
            if temp[j][i] == t:
                cnt += 1
            else:
                t = temp[j][i]
                cnt = 1
            if cnt >= K:
                break
        else:
            return False
        cnt = 0
    return True

def f(n, k, m, z):
    if n == m:
        if fac(0, m, [0]*m, p) == m:
            return m
    else:
        for i in range(z, k):
            if used[i] == 0:
                p[n] = i
                used[i] = 1
                if f(n+1, k, m, i) == m:
                    return m
                used[i] = 0

def fac(n, k, temp, temp_2):
    if n == k:
        if change(temp, temp_2):
            return k
    else:
        for i in range(2):
            temp[n] = i
            if fac(n+1, k, temp, temp_2) == k:
                return k

def change(cl, pl):
    temp = make_temp()
    n = len(pl)
    for i in range(n):
        temp[pl[i]] = [cl[i]] * len(temp[i])
    return check(temp)



def make_temp():
    global D
    temp = []
    for i in range(D):
        temp.append(board[i].copy())
    return temp

T = int(input())
for t in range(1, T+1):
    D, W, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(D)]
    res = 0
    for i in range(D):
        p = [0] * i
        used = [0] * D
        if f(0, D, i, 0) != None:
            res = i
            break
    print("#{} {}".format(t, res))
