
def spring():
    global array, field, death_idxs
    for row in range(1, N+1):
        for col in range(1, N+1):
            if len(field[row][col]) != 0:
                wood = field[row][col]
                for idx in range(len(wood)-1, -1, -1):
                    if wood[idx] != 0 and array[row][col] >= wood[idx]:
                        array[row][col] -= wood[idx]
                        wood[idx] += 1
                    elif wood[idx] != 0 and array[row][col] < wood[idx]:
                        energy = field[row][col][idx] // 2
                        array[row][col] += energy
                        field[row][col][idx] = 0

def autumn():
    global array, field, di, dj
    for row in range(1, N+1):
        for col in range(1, N+1):
            for wood in field[row][col]:
                if wood >= 5 and wood % 5 == 0:
                    for d in range(8):
                        ni = row + di[d]
                        nj = col + dj[d]
                        if 1 <= ni < N+1 and 1 <= nj < N+1:
                            field[ni][nj].append(1)
def winter():
    global array, charge
    for row in range(1, N+1):
        for col in range(1, N+1):
            array[row][col] += charge[row][col]

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]
N, M, K = map(int, input().split())
charge = [[0]*(N+1)] + [[0]+list(map(int, input().split())) for _ in range(N)]
array = [[0]*(N+1)] + [[5]*(N+1) for _ in range(N)]
woods = [list(map(int, input().split())) for _ in range(M)]
field = [[[] for _ in range(N+1)] for _ in range(N+1)]
# 나무 심
for wood in woods:
    field[wood[0]][wood[1]].append(wood[2])
# k년 이 지난 후
for y in range(K):
    death_idxs = []
    spring()
    autumn()
    winter()

cnt = 0
for r in range(1,N+1):
    for c in range(1, N+1):
        for wood in field[r][c]:
            if wood != 0:
                cnt += 1
print(cnt)
