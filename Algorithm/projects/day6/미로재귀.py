def checkmove(x, y):
    global N
    global board
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    if board[x][y] == 3:
        return 1 # 완료
    else:
        board[x][y] = "1" # 지나온곳을 벽으로 바꾼다.
        for i in range(4):
            x_ = x + di[i]
            y_ = y + dj[i]
        if 0 <= x_ < N and 0 <= y_ < N:
            if board[x][y] != "1": # 벽이아니면 이동
                if checkmove(x_, y_) == 1:
                    return 1
    return 0
