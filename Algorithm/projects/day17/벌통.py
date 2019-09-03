import sys

sys.stdin = open('honey.txt', 'r')

def check_honey(i, M, C):
    global board
    for j in range(N-M):
        select = board[i][i+j+1]



T = int(input())
for t in range(1, T+1):
    # 벌통크기, 벌통 개수, 최대양
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
