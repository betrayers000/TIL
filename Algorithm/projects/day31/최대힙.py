import sys

sys.stdin = open('maxheap.txt', 'r')


def get_last():
    if q == []:
        return 0
    return len(q)


def enque(val):
    global q
    q.append(val)
    n = get_last()
    par = n // 2
    while par != 0:
        if q[par - 1] < q[n - 1]:
            q[par - 1], q[n - 1] = q[n - 1], q[par - 1]
        else:
            return
        n = par
        par = n // 2


def deque():
    global q
    if q == []:
        return 0
    res = q[0]
    q[0], q[-1] = q[-1], q[0]
    q = q[:-1]
    n = 1
    idx = get_last()
    while n*2 <= idx:
        c1, c2 = n*2, n*2+1
        if c2 > idx:
            q[n-1], q[c1-1] = q[c1-1], q[n-1]
            n = c1
        else:
            if q[c1-1] > q[c2-1]:
                if q[n-1] < q[c1-1]:
                    q[n-1], q[c1-1] = q[c1-1], q[n-1]
                    n = c1
                else:
                    return res
            else:
                if q[n-1] < q[c2-1]:
                    q[n-1], q[c2 - 1] = q[c2 - 1], q[n-1]
                    n = c2
                else:
                    return res
    return res




N = int(input())
q = []
for _ in range(N):
    n = int(input())
    if n == 0:
        print(deque())
    else:
        enque(n)