import sys

sys.stdin = open('input.txt', 'r')


# 상 우 하 좌 1, 2, 3, 4
def get_charging_area(charge):
    x, y, d, e = charge
    x -= d
    y -= d
    result = []
    n = d * 2 + 1
    start, end = 0, 0
    for i in range(n):
        if i <= d:
            start = d - i
            end = d + i + 1
        else:
            start = i - d
            end = n - i + d
        for j in range(start, end):
            if 0 < x + i < 11 and 0 < y + j < 11:
                result.append([y + j, x + i])
    return result


def get_path(point, way):
    x, y = point
    if way == 1:
        if 0 < x - 1 < 11:
            x = x - 1
    elif way == 2:
        if 0 < y + 1 < 11:
            y = y + 1
    elif way == 3:
        if 0 < x + 1 < 11:
            x = x + 1
    elif way == 4:
        if 0 < y - 1 < 11:
            y = y - 1
    return [x, y]


def matching(point):
    global area, A, chager, M
    temp = [[0] for _ in range(M+1)]
    for p in range(M+1):
        for i in range(A):
            if point[p] in area[i]:
                if temp[p] != [0]:
                    temp[p] = [temp[p][0], chager[i][3]]
                else:
                    temp[p] = [chager[i][3]]
    return temp


T = int(input())
for t in range(1, T+1):
    M, A = map(int, input().split())
    way_a = list(map(int, input().split()))
    way_b = list(map(int, input().split()))
    chager = [list(map(int, input().split())) for _ in range(A)]
    area = [[0] for _ in range(A)]
    for i in range(A):
        area[i] = get_charging_area(chager[i])
    start_a = [1, 1]
    point_a = [start_a]
    for a in way_a:
        start_a = get_path(start_a, a)
        point_a.append(start_a)
    start_b = [10, 10]
    point_b = [start_b]
    for b in way_b:
        start_b = get_path(start_b, b)
        point_b.append(start_b)
    result = list(zip(matching(point_a), matching(point_b)))
    total = 0
    for r in result:
        a, b = r
        if len(a+b) == 3:
            total += sum(set(a+b))
        else:
            total += a[0] + b[0]
    print(total)
