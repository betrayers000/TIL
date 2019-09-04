#6109번 추억의 2048게임
import sys
sys.stdin = open('2048.txt', 'r')

for tc in range(int(input())):
    N, how = input().split()
    N = int(N)
    cross = [list(map(int, input().split())) for _ in range(N)]

    board = []
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(cross[j][i])
        board.append(temp)
    for b in board:
        for z in range(1, N):
            if b[z-1] == b[z]:
                b[z-1] = b[z] * 2
                b[z] = 0

