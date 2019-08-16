T = int(input())
for t in range(1, T + 1):
    N = int(input())
    color = [[int(i) for i in input().split()] for n in range(N)]
    board = [[0 for i in range(10)] for j in range(10)]
    for c in color:
        x1, y1, x2, y2, b = c
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                # 1이 먼저가 아니라 2가 먼저일경우도 있다.
                if board[x][y] != 0 and board[x][y] != b:
                    board[x][y] = 3
                else :
                    board[x][y] = b
    count = 0
    for boad in board:
        temp = 0
        for z in boad:
            if z == 3:
                temp +=1
        count += temp
    print(f"#{t} {count}")