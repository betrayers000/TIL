import sys

sys.stdin = open("input.txt", "r")


# 방향을 체크하는 함수
# 0이면 밑방향, 2면 왼쪽 3이면 오른쪽
# 들어오는 c는 이전에 어느방향에서 움직였냐를 확인.
# c를 확인하고 다음 방향을 정한다.
def check(board, x, y, c):
    if c == 0:
        if y == 0:
            if board[x][y + 1] == 1:
                return 3
        elif y == 99:
            if board[x][y-1] == 1:
                return 2
        else:
            if board[x][y-1] == 1:
                return 2
            elif board[x][y + 1] == 1:
                return 3
    elif c == 2:
        if y > 0:
            if board[x][y-1] == 1:
                return 2
    elif c == 3:
        if y < 99:
            if board[x][y+1] == 1:
                return 3
    return 0




for t in range(1, 11):
    n = int(input())
    board = [list(map(int, input().split())) for i in range(100)]
    # start포인트를 정한다.
    start = []
    for i in range(100):
        if board[0][i] == 1:
            start.append((0, i))
    result = 0
    # start포인트를 반복돌리면서 하나씩 돌린다.
    for sp in start:
        x, y = sp
        c = 0
        end = 0
        # x 가 99가 되면 맨밑에 도달했기 떄문에 반복 정지
        while x != 99:
            c = check(board, x, y, c)
            # check함수를 이용해서 검사하고 이동방향으로 이동을 해준다.
            if c == 2:
                y -= 1
            elif c == 3:
                y += 1
            else :
                x += 1
            # end에 마지막값을 넣어준다.
            # 해당값이 2이면 도착이기때문에 체크를 위함
            end = board[x][y]
        print(sp, end)
        if end == 2:
            result = sp[1]
    print(result)


