import sys

sys.stdin = open('shark.txt', 'r')


def get_distance(shark, val):
	global board, size, N, temp
	dx = [0, 1, 0, -1]
	dy = [1, 0, -1, 0]
	q = [0] *(N*N)
	visited = [[0] * N for _ in range(N)]
	front, rear = -1, -1
	rear += 1
	q[rear] = shark
	visited[shark[0]][shark[1]] = 1
	while front != rear:
		front += 1
		x, y = q[front]
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx == val[0] and ny == val[1]:
				return visited[x][y]
			if 0 <= nx < N and 0 <= ny < N:
				if board[nx][ny] <= size and visited[nx][ny] == 0:
					visited[nx][ny] = visited[x][y] + 1
					rear += 1
					q[rear] = [nx, ny]


def get_distance_list(shark, fish, size):
	global board
	dist = []
	for idx, val in enumerate(fish):
		fx, fy = val
		if board[fx][fy] < size:
			gets = get_distance(shark, val)
			if gets == None:
				continue
			dist.append([fx, fy, idx, gets])
	return dist


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
fish = []
shark = 0
size = 2
temp = 0
for i in range(N):
	for j in range(N):
		if board[i][j] != 0:
			if board[i][j] == 9:
				shark = [i, j]
			else:
				fish.append([i, j])
board[shark[0]][shark[1]] = 0
if fish == []:
	print(0)
else:
	cnt = 0
	size_cnt = 0
	while 1:
		if fish == []:
			break
		dist = get_distance_list(shark, fish, size)
		if dist == []:
			break
		check = sorted(dist, key=lambda x: (x[3], x[0], x[1]))[0]
		shark = [check[0], check[1]]
		fish.pop(check[2])
		size_cnt += 1
		cnt += check[3]
		if size_cnt == size:
			size += 1
			size_cnt = 0
	# print(fish)
	print(cnt)
