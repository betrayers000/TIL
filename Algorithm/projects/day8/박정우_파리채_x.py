# x모양

import sys

sys.stdin = open('fly.txt', 'r')

def getfly_cross(x, y, M):
    # 왼쪽 끝값과 오른쪽 끝값을 초기화 해준다.
    left = x, y
    right = x, y + M -1
    total = 0
    # 작업완료된 좌표를 담을 리스트를 만들어준다
    point = []
    # 파리채만큼 반복을 돌리면서 작업을 해주고 point 리스트에 중복없이 넣어준다
    for i in range(M):
        left_ = [left[0]+i, left[1]+i]
        right_ = [right[0]+i, right[1]-i]
        if left_ not in point:
            point.append(left_)
        if right_ not in point:
            point.append(right_)
    # point를 반복을 돌려서 더해준다.
    for p in point:
        total += board[p[0]][p[1]]
    return total

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(N)]
    total_ = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = getfly_cross(i, j, M)
            if total_ < total:
                total_ = total
    print(total_)