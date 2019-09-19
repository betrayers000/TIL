import sys

sys.stdin = open('cell.txt', 'r')

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def insertion1(x, y, life, server):
    if server.get(y):
        if server[y].get(x):
            return False
        else:
            server[y][x] = [life, life]
            return True
    else:
        server[y] = {x: [life, life]}
        return True


def insertion2(x, y, life, server):
    if server.get(y):
        if server[y].get(x):
            if server[y][x][0] < life:
                server[y][x] = [life, life]
        else:
            server[y][x] = [life, life]
    else:
        server[y] = {x: [life, life]}

T = int(input())
for tc in range(1):
    size_y, size_x, limit_time = map(int, input().split())
    initial = [list(map(int, input().split())) for _ in range(size_y)]

    table_current = {}  # {좌표 y: 좌표x: [Life_Cycle, current(Life_Cycle~-Life_Cycle)]}
    table_temp = {}  # 위와 같은 형식
    alive_cells = []  # [[좌표1], [좌표2]]

    cnt = 0
    for y in range(size_y):
        for x in range(size_x):
            if initial[y][x]:
                alive_cells.append([x, y])
                insertion1(x, y, initial[y][x], table_current)
                cnt += 1

    for time in range(limit_time):
        table_temp = {}
        for candidate in reversed(alive_cells):
            x, y = candidate
            table_current[y][x][1] -= 1
            if table_current[y][x][1] == - table_current[y][x][0]:
                alive_cells.remove([x, y])
                cnt -= 1
            elif table_current[y][x][1] == -1:
                for _ in range(4):
                    new_x, new_y = x + dx[_], y + dy[_]
                    insertion2(new_x, new_y, table_current[y][x][0], table_temp)
        for y in table_temp.keys():
            for x, value in table_temp[y].items():
                if insertion1(x, y, value[0], table_current):
                    alive_cells.append([x, y])
                    cnt += 1

    print("#{} {}".format(tc + 1, cnt))