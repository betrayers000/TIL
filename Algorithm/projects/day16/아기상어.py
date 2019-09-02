import sys

sys.stdin = open('shark.txt', 'r')


def get_dist(shark, fish, size):
    global board
    x, y = shark
    dist = []
    for idx, val in enumerate(fish):
        fx, fy = val
        if board[fx][fy] < size:
            if fx == x:
                dist.append([fx, fy, idx, abs(fy - y)])
            elif fy == y:
                dist.append([fx, fy, idx, abs(fx - x)])
            else:
                dist.append([fx, fy, idx, abs(x - fx) + abs(fy - y)])
    return dist


def check_dist(shark, dist):
    x, y = shark
    result = []
    print(dist)
    dist = sorted(dist, key=lambda x: x[3])
    if len(dist) == 1:
        result.extend(dist[0])
    else:
        bd = dist[0][3]
        div = 0
        for i in range(len(dist)):
            if bd != dist[i][3]:
                div = i
                break
        dist = dist[:div]
        print(dist)
    return result


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
fish = []
shark = 0
size = 2
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            if board[i][j] == 9:
                shark = [i, j]
            else:
                fish.append([i, j])
if fish == []:
    print(0)
else:
    cnt = 0
    size_cnt = 0
    print(fish)
    while 1:
        if fish == []:
            break
        dist = get_dist(shark, fish, size)
        if dist == []:
            break
        check = check_dist(shark, dist)
        print(shark, check, fish, size)
        shark = [check[0], check[1]]
        fish.pop(check[2])
        size_cnt += 1
        cnt += check[3]
        if size_cnt == size:
            size += 1
            size_cnt = 0
    print(cnt)
