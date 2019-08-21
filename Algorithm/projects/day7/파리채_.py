
def getfly(x, y, M):
    global board
    total = 0
    y_ = y + M
    x_ = y + M
    for j in range(1, M):
        total += board[x][y+j]
        total += board[x+j][y]
        total += board[x_+j][y_]
        total += board[x_][y_+j]
    total += board[x][y]
    total += board[x_][y_]

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(N)]


