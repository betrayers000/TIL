import sys

sys.stdin = open('cook.txt', 'r')



def f(n, k, m, z):
    global minV, board, N, cnt
    if n == m:
        sub_set.append(p.copy())
        return
    else:
        for i in range(z, k):
            if used[i] == 0:
                used[i] = 1
                p[n] = i
                f(n+1, k, m, i)
                used[i] = 0

def f2(dish, n, k, m):
    global minV, board, N, cnt
    if n == m:
        temp.append(board[q[0]][q[1]])
        return
    else:
        for i in range(k):
            if used_[i] == 0:
                used_[i] = 1
                q[n] = dish[i]
                f2(dish, n+1, k, m)
                used_[i] = 0



T = int(input())
for t in range(1, 2):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    p = [0] * (N//2)
    sub_set = []
    cnt = 0
    minV = board[0][-1]
    f(0, N, N//2, 0)
    div = len(sub_set)//2
    a_dish = sub_set[:div]
    b_dish = sub_set[div:][::-1]
    q = [0] * 2
    used_ = [0] * (N//2)
    result = []
    for i in range(div):
        temp = []
        f2(a_dish[i], 0, N//2, 2)
        f2(b_dish[i], 0, N//2, 2)
        div_ = len(temp)//2
        result.append(abs(sum(temp[:div_]) - sum(temp[div_:])))
    print(min(result))