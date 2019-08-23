import sys

sys.stdin = open('input.txt', 'r')


def get_numbers(depth, idx):
    global result
    global temp

    if depth == 6:
        result.append(temp)
        temp = []
        return 1
    else:
        for i in range(N):
            if i != idx:
                temp.append(S[i])
            if get_numbers(depth+1, i) == 1:
                return




while True:
    K = list(map(int, input().split()))
    if K == [0]:
        break
    S = []
    N = 0
    for k in range(K[0]+1):
        if k == 0:
            N = K[k]
        else:
            S.append(K[k])
    result = []
    temp = []
    get_numbers(1, -1)



