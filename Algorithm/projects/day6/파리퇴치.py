def getfly(i, j):
    global board
    global M
    total = 0
    for x in range(M):
        for y in range(M):
            total += board[i+x][j+y]

    return total


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(N)]
    maxfly = 0
    for i in range(N-M):
        for j in range(N-M):
            total = getfly(i, j)
            if maxfly < total:
                maxfly = total
    print(maxfly)
