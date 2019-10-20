import sys

sys.stdin = open('center.txt', 'r')

def put_receipt(s, cl):
    global top
    temp = 0
    for i in range(N):
        n, re = receipt_info[i][-1]
        if re <= s:
            temp = i
            receipt_info[i].append((top+1, cl+receipt[i]))
            time.append(cl+receipt[i])
            if re != 0:
                return put_repair(s, re, n)
            return True
    client[top] = receipt_info[temp][-1][-1]
    return False

def put_repair(s, cl, n):
    global last_repair
    for i in range(M):
        if repair_info[i][-1][-1] <= s:
            repair_info[i].append((n, cl+repair[i]))
            last_repair = cl+repair[i]
            return True
    wait.append((n, last_repair))

def check(s):
    for i in range(N):
        n, r = receipt_info[i][-1]
        if r == s:
            return put_repair(s,r,n)

T = int(input())
for t in range(1, 2):
    N, M, K, A, B = map(int, input().split())
    receipt = [map(int, input().split()) for _ in range(N)]
    repair = [map(int, input().split()) for _ in range(M)]
    receipt_info, repair_info = [[(0, 0)]*N], [[(0, 0)]*M]
    time = []
    wait = []
    last_repair = 99
    # for _ in range(M):
    #     repair_info += [[]].copy()
    # for _ in range(N):
    #     receipt_info += [[]].copy()
    client = list(map(int, input().split()))
    top = 0
    sec = 0
    while last_repair >= sec:
        sec += 1
        if top < K and sec == client[top]:
            if put_receipt(sec, client[top]):
                top += 1
        if time != [] and sec in time:
            check(sec)
        print(client, top, sec)
    print(sec, receipt_info, repair_info)


