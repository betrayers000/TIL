import sys

sys.stdin = open('input.txt', 'r')

def getboard(x, y, s, visited):
    global board
    global N
    global ans
    global result
    s += board[x][y]
    if x == N-1:
        visited[y] = 0
        result.append(s)
        if ans > s:
            ans = s
        return 1
    for i in range(N):
        if i != y and visited[i] != 1:
            visited[i] = 1
            if getboard(x+1, i, s, visited) == 1:
                visited[y] = 0
                return
            else:
                visited[y] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for n in range(N)]
    ans = 99
    result = []
    for i in range(N):
        visited = [0] * N
        visited[i] = 1
        getboard(0, i, 0, visited)
    print(result)
    print(f"#{t} {ans}")
