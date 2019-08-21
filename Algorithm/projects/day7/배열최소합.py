import sys

sys.stdin = open('input.txt', 'r')

def swap(per, i, depth):
    per[i], per[depth] = per[depth], per[i]

def permutation(per, depth, n, k):
    global result
    if depth == k:
        result.append(per)
        return
    else:
        for i in range(depth):
            swap(per, i, depth)
            permutation(per, depth+1, n, k)
            swap(per, i, depth)



T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for n in range(N)]
    board_list = list(range(1, N+1))
    result = []
    per = []
    permutation(per, 0, N, N)
    print(result)








