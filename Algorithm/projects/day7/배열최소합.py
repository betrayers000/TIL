import sys


sys.stdin = open('input.txt', 'r')


def getboard(x, y, s):
    global board
    global N
    global visited
    global result
    s += board[x][y]
    if x == N-1:
        visited = [0] * N
        result.append(s)
        return 1
    for i in range(N):
        if i != y and visited[i] != 1:
            visited[i] = 1
            if getboard(x+1, i, s) == 1:
                return

T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for n in range(N)]
    result = []
    for i in range(N):
        visited = [0] * N
        print(getboard(0, i, 0))
    print(result)
    print(visited)











