import sys

sys.stdin = open('wood.txt', 'r')

dx = [0, 1, 0, -1, -1, 1, 1, -1]
dy = [1, 0, -1, 0, -1, -1, 1, 1]

def growth(temp):
    a = set()
    for i in temp:
        x, y = i
        b = sorted(wood[x-1][y-1], reverse=False)
        c =[]
        total = 0
        for year in b:
            if land[x-1][y-1] >= year:
                a.add((x, y))
                c.append(year+1)
                # print(b, year, land[x-1][y-1], c)
                land[x-1][y-1] -= year
            else:
                total += year//2
        wood[x-1][y-1] = c
        land[x-1][y-1] += total
    return a

def breed(temp):
    global N
    a = set()
    for i in temp:
        x, y = i
        b = wood[x-1][y-1]
        for z in b:
            if z % 5 == 0:
                for k in range(8):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx-1 < N and 0<= ny-1 < N:
                        a.add((nx, ny))
                        wood[nx-1][ny-1].append(1)
        a.add((x, y))
    return a

def give():
    global food
    for i in range(N):
        for j in range(N):
            land[i][j] += food[i][j]

N, M, K = map(int, input().split())
food = [list(map(int, input().split())) for _ in range(N)]
info = set()
land = [[5] * N for _ in range(N)]
wood = []
for _ in range(N):
    wood += [[]].copy()
for i in range(N):
    for j in range(N):
        wood[i].append([])
for _ in range(M):
    x, y, z = (map(int, input().split()))
    wood[x-1][y-1].append(z)
    info.add((x, y))

yer = 0
# print(info)
# print(wood)
while yer < K:
    if info == set():
        break
    for i in range(3):
        if i == 0:
            # 자기 나이만큼 양분을 흡수하고 1살 먹는다/ 양분이 없으면 죽는다
            # 죽은 나무가 양분이 된다. 죽은 나무의 나이 //2
            # 나무가 여러개 있으면 가장 나이가 적은 나무가 양분을 흡수한다.
            info = growth(info)
        elif i == 1:
            # 5의 배수일시에 주변으로 나이가 1인 나무가 생긴다.
            info = breed(info)
        elif i == 2:
            # 땅에 양분이 추가 된다 양분은 info
            give()
    # print(info)
    # print(land)
    # print(wood)
    yer += 1
# print(info)
total = 0
if info != set():
    for i in range(N):
        for j in range(N):
            total += len(wood[i][j])
print(total)