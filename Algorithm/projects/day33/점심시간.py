import sys

sys.stdin = open('lunch.txt', 'r')


def f(n, k):
    global minV
    if n == k:
        left, right = [], []
        for j in range(len(p)):
            if p[j] == 0:
                left.append(j)
            else:
                right.append(j)
        solv = moving(left, right)
        if minV > solv:
            minV = solv
        return
    else:
        p[n] = 1
        f(n + 1, k)
        p[n] = 0
        f(n + 1, k)


def moving(left, right):
    lx, ly = s[0]
    rx, ry = s[1]
    rh = board[rx][ry]
    lh = board[lx][ly]
    left_table = []
    right_table = []
    for i in left:
        x, y = h[i]
        dis = abs(lx - x) + abs(ly - y)
        left_table.append([x, y, dis])
    for i in right:
        x, y = h[i]
        dis = abs(rx - x) + abs(ry - y)
        right_table.append([x, y, dis])
    left_table.sort(key=lambda x: x[2])
    right_table.sort(key=lambda x: x[2])
    sec = 0
    visited_left = [0] * len(left)
    visited_right = [0] * len(right)
    escape_left = [0] * len(left)
    escape_right = [0] * len(right)
    # print(right_table)
    left_temp = []
    right_temp = []
    # print(left, right)
    while 1:
        # print(left_temp, right_temp)
        # print(visited_left, visited_right)
        # print(escape_left, escape_right)
        for i in range(len(visited_left)):
            if sec == visited_left[i] and visited_left[i] != 0:
                escape_left[i] = 1
        for i in range(len(visited_right)):
            if sec == visited_right[i] and visited_right[i] != 0:
                escape_right[i] = 1
        if sum(escape_left) == len(left) and sum(escape_right) == len(right):
            break
        for i in range(len(right_table)):
            x, y, w = right_table[i]
            a = check(visited_right, escape_right)
            if visited_right[i] == 0:
                if w == sec and a < 3:
                    visited_right[i] = sec + rh + 1
                elif w == sec and a > 2:
                    right_temp.append(a)
                else:
                    if right_temp != [] and a < 3:
                        right_temp.pop()
                        visited_right[i] = sec + rh
        for i in range(len(left_table)):
            x, y, w = left_table[i]
            a = check(visited_left, escape_left)
            if visited_left[i] == 0:
                if w == sec and a < 3:
                    visited_left[i] = sec + lh + 1
                elif w == sec and a > 2:
                    left_temp.append(a)
                else:
                    if left_temp != [] and a < 3:
                        left_temp.pop()
                        visited_left[i] = sec + lh
        sec += 1
    # print(left, right, left_table, right_table)
    # print(sec, visited_left, visited_right, lh, rh)
    return sec


def check(v, e):
    cnt = 0
    for i in range(len(v)):
        if v[i] != 0 and e[i] == 0:
            cnt += 1
    return cnt


T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    h = []
    s = []
    minV = 9999999
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                h.append([i, j])
            elif board[i][j] > 1:
                s.append([i, j])
    nh = len(h)
    p = [0] * nh
    f(0, nh)
    print("#{} {}".format(t, minV))
