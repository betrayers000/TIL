import sys

sys.stdin = open('heap.txt', 'r')

def get_last():
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
        return -1
    res = q[0]
    q[0], q[-1] = q[-1], q[0]
    q.pop()
    n = 1
    idx = get_last()
    while n*2+1 <= idx:
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


T = int(input())
for t in range(1, T+1):
    q = []
    N = int(input())
    res = []
    for _ in range(N):
        com = list(map(int, input().split()))
        if len(com) == 1:
            res.append(deque())
        else:
            enque(com[1])
    print("#{} {}".format(t, ' '.join(map(str, res))))