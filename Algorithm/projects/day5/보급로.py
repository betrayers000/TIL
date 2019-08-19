import sys

sys.stdin = open("input.txt", "r")



def getdeep(board, x, y):
    pass


T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(input()) for n in range(N)]
    print(board)
