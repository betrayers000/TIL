board = [[2, 7, 4, 3, 6],
         [8, 5, 8, 3, 2],
         [2, 2, 3, 6, 9],
         [5, 9, 2, 5, 7],
         [3, 6, 2, 9, 4]]

M = 5
# 각방향마다 바뀌는 값
# 우하좌상 순
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


for i in range(M):
    for j in range(M):
        # 방향이 4방향
        for z in range(3):
            ni = i + di[z]
            nj = j + dj[z]
            if ni>=0 and ni < M and nj>=0 and ni < M:

