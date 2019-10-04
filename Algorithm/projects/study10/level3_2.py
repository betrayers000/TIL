def get_used(p):
    for i in range(len(p)):
        x, y = i, p[i]



def f(n, k):
    global used, p
    if n == k:
        print(p)
        return
    else:
        for i in range(k):
            if used[i] == 0:
                p[n] = i
                f(n+1, k)
                p[n] = 0




def solution(n):
    global used, p
    answer = 0
    used = [0] * 24
    p = [0] * n
    f(0, 4)
    return answer

solution(4)
