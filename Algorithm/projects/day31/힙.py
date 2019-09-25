import sys

sys.stdin = open('heap.txt', 'r')


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


def del_sort(n):
    idx = get_last()
    while n < idx:
        ch1 = n * 2
        ch2 = n * 2 + 1
        if q[ch2-1] == []:
            q[n], q[ch1-1] = q[ch1-1], q[n]
            n = ch1
        else:
            if q[n-1] < q[max(ch1 - 1, ch2 - 1)]:
                q[n-1], q[max(ch1 - 1, ch2 - 1)] = q[max(ch1 - 1, ch2 - 1)], q[n-1]
                n = max(ch1, ch2)

def deque():
    global q
    if q == []:
        return -1
    res = q[0]
    q[0], q[-1] = q[-1], q[0]
    q = q[:-1]
    del_sort(1)
    return res



T = int(input())
for t in range(1, T + 1):
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
