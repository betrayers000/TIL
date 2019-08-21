def getfly(i, j, M):
    global board
    total = 0
    for x in range(M):
        for y in range(M):
            total += board[i+x][j+y]
    return total


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(N)]
    maxfly = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = getfly(i, j, M)
            maxfly.append(total)
    if M >= 3:
        maxfly_in = []
        for i in range(1, N-M+2):
            for j in range(1, N-M+2):
                total = getfly(i, j, M-2)
                maxfly_in.append(total)
        max_ = []
        for z in range(len(maxfly)):
            max_.append(maxfly[z] - maxfly_in[z])
        result = max(max_)
    else:
        result = max(maxfly)
    print(f"#{t} {result}")