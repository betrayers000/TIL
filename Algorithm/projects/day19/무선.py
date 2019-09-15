import sys

sys.stdin = open('input.txt', 'r')


class Node:

    def __init__(self, x, y, size, index):
        self.x = x
        self.y = y
        self.size = size
        self.index = index


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
    global area, A, charge_list, M
    temp = [[0] for _ in range(M + 1)]
    for p in range(M + 1):
        x, y = point[p]
        for i in range(len(charge_list)):
            chager = charge_list[i]
            if temp[p] != [0]:
                if chager.x == x and chager.y == y:
                    temp[p] = temp[p] + [chager]
            else:
                if chager.x == x and chager.y == y:
                    temp[p] = [chager]
    return temp


def check_overlap(p):
    a, b = p
    if a == [0]:
        a[0] = Node(-1, -1, 0, -1)
    if b == [0]:
        b[0] = Node(-1, -1, 0, -1)
    result = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i].index != b[j].index:
                charge_sum = a[i].size + b[j].size
                if result < charge_sum:
                    result = charge_sum
            else:
                if result < a[i].size:
                    result = a[i].size
    return result



T = int(input())
for t in range(1, T+1):
    M, A = map(int, input().split())
    way_a = list(map(int, input().split()))
    way_b = list(map(int, input().split()))
    chager = [list(map(int, input().split())) for _ in range(A)]
    area = [[0] for _ in range(A)]
    for i in range(A):
        area[i] = get_charging_area(chager[i])
    charge_list = []
    for j in range(A):
        for ar in area[j]:
            charge_list.append(Node(ar[0], ar[1], chager[j][3], j))
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
        z = check_overlap(r)
        total += z
    print(total)
