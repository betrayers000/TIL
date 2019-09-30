U = 3
L = 2
C = [2, 1, 1, 0, 1]

def f(n, k, res):
    if n == k:
        print(res)
        return
    else:


def solution(U, L, C):
    res = [[0] * len(C) for _ in range(2)]
    f(0, len(C), res)


solution(U,L,C)