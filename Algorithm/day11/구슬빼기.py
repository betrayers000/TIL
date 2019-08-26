import sys

sys.stdin = open('input.txt', 'r')


def bfs(start, N, M):
    global board
    # 큐를 초기화해준다.
    q = [0] * 5000
    front, rear = 0, 0
    rear = (rear + 1) % 5000
    q[rear] = start
    dirs = [0, 1, 2, 3]
    while front != rear:
        front = (front + 1) % 5000
        point = q[front]
        # 큐에서 포인트를 뽑아준다 앞부분이 레드포인트 뒤가 블루포인트
        rx, ry, rd = point[0]
        bx, by, bd = point[1]
        check = [0, 0]
        for z in range(4):
            # 일단 받은 포인트를 체크한다. R, B의 위치를 확인
            f = point_check(point, dirs[z])
            # 위치를 확인한뒤에 순서대로 움직여준다
            if f == "r":
                next_ = move(point[0], dirs[z], N, M)
                nx, ny, nd = next_
                # 레드 부터 움직여야 할경우 움직여준뒤 움직인 좌표에 R을 놓아주고
                board[nx][ny] = "R"
                next__ = move(point[1], dirs[z], N, M)
                rx_, ry_, rd_ = next_
                bx_, by_, bd_ = next__
            else:
                # 위와 동일인데 블루부터 움직인다.
                next__ = move(point[1], dirs[z], N, M)
                nx, ny, nd = next__
                board[nx][ny] = "B"
                next_ = move(point[0], dirs[z], N, M)
                bx_, by_, bd_ = next__
                rx_, ry_, rd_ = next_
            # 모든 처리가 끝난뒤에 위에 표시했던 R과 B를 제거해준다.
            board[rx_][ry_] = "."
            board[bx_][by_] = "."
            # 둘이 동시에 빠졌을때 실패 둘이 동시에 빠질경우도 -1이네 ..?
            if rx_ == 0 and ry_ == 0 and bx_ == 0 and by_ == 0:
                check[0] += 1
            # 빨간구슬만 빠졌을때 무조건 -1 이하가 나온다.
            elif rx_ == 0 and ry_ == 0 and bx_ != 0 and by_ != 0:
                check[0] -= 4
                check[1] = rd_
            # 파란구슬만 빠졌을때 실패 4방향 전부 실패했을때 check[0] 은 4가 된다.
            elif rx_ != 0 and ry_ != 0 and bx_ == 0 and by_ == 0:
                check[0] += 1
            # 반환 좌표가 이전좌표와 똑같을때는 넘어간다. 실행 시간 단축을 위해서
            elif rx_ == rx and ry == ry_ and bx == bx_ and by_ == by:
                continue
            # 위의 경우를 다 통과한경우 보드에서 R,B를 지워주고 q에 좌표를 넣어준다.
            if bd_ > 10 or rd_ > 10:
                return -1
            if bx_ == 0 and by_ == 0:
                continue
            rear = (rear + 1) % 5000
            q[rear] = [next_, next__]
        if check[0] == 4:
            return -1
        elif check[0] < 0:
            return check[1]

    return -1


def move(point, dir, N, M):
    # 이동을 한다. 포인트에서 x, y, d 를가져온다.
    x, y, d = point
    # 좌우상하 0, 1, 2, 3 순서이다.
    # 각 순서 마다 좌우의 경우에는 M만큼(한줄의 길이) 이동하면서 "." 이아닐때까지 이동한다.
    # 상하의 경우에는 N만큼(줄의 개수) 이동하면서 "." 이 아닐때까지 이동한다.
    # O를 만날경우에는 0,0을 넣어줌으로써 빠졌다는걸 확인해준다.
    # 반환할때는 현재좌표말고 이전좌표를 반환해줘야한다.
    if dir == 0:
        for m in range(1, M):
            y_ = y - m
            if board[x][y_] == "O":
                return [0, 0, d + 1]
            if board[x][y_] != ".":
                return [x, y_ + 1, d + 1]
    elif dir == 1:
        for m in range(1, M):
            y_ = y + m
            if board[x][y_] == "O":
                return [0, 0, d + 1]
            if board[x][y_] != ".":
                return [x, y_ - 1, d + 1]
    elif dir == 2:
        for n in range(1, N):
            x_ = x - n
            if board[x_][y] == "O":
                return [0, 0, d + 1]
            if board[x_][y] != ".":
                return [x_ + 1, y, d + 1]
    elif dir == 3:
        for n in range(1, N):
            x_ = x + n
            if board[x_][y] == "O":
                return [0, 0, d + 1]
            if board[x_][y] != ".":
                return [x_ - 1, y, d + 1]


# 포인트의 위치를 체크한다. 구슬의 위치에 따라 어느 구슬이 더 먼저 이동해야하는지 정한다.
# ex > 왼쪽방향일때는 빨간구슬이 파란구슬보다 왼쪽에 있으면 먼저 움직인다.
def point_check(point, dir):
    rx, ry, rd = point[0]
    bx, by, bd = point[1]
    if dir == 0:
        if ry > by:
            return "b"
        else:
            return "r"
    elif dir == 1:
        if ry > by:
            return "r"
        else:
            return "b"
    elif dir == 2:
        if rx > bx:
            return "b"
        else:
            return "r"
    elif dir == 3:
        if rx > bx:
            return "r"
        else:
            return "b"


N, M = map(int, input().split())
board = [list(input()) for n in range(N)]

red = 0
blue = 0
# R, B의 위치를 찾아주고 해당위치를 "." 으로 초기화해준다.
for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            red = [i, j, 0]
            board[i][j] = "."
        elif board[i][j] == "B":
            blue = [i, j, 0]
            board[i][j] = "."

start = [red, blue]
print(bfs(start, N, M))
