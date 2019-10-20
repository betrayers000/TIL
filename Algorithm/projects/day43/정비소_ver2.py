import sys

sys.stdin = open('center.txt', 'r')

minV = 9999999
minX = 0
minV_2 = 999999
minX_2 = 0

def put_receipt(n, t):
    global minV, minX
    minV = 999999
    ch = False
    for i in range(N):
        # 접수처에 인원이 없는경우
        to, a = receipt_dic[i]
        # 최소 값을 찾고, 한명이라도 들어갔으면 더이상 안들어가기때문에
        # 빈 접수처가 여러개 있을 시를 위한 처리
        if a == 0 and not ch:
            rec[i].append(n)
            receipt_dic[i] = (n, t + receipt[i])
            ch = True
        if minV > receipt_dic[i][1] and receipt_dic[i][1] != 0:
            minV = receipt_dic[i][1]
            minX = i
    if ch:
        return True
    # 접수처가 가득 차있는 경우
    # 고객의 시간을 가장 빨리 끝나는 시간까지 증가시킨다
    # mp = minV - client[n-1]
    # for i in range(n-1, len(client)):
    #     client[i] += mp
    return False

def check(t):
    global minX, N, minV
    temp = 999999
    for i in range(N):
        to, a = receipt_dic[i]
        if a == t:
            receipt_dic[i] = (0, 0)
            put_repair(to, t)
        if receipt_dic[i][1] < temp and receipt_dic[i][1] != 0:
            temp = receipt_dic[i][1]
    minV = temp

def check_2(t):
    global minV_2, minX_2, M, cnt
    temp = 99999
    chc = False
    for i in range(M):
        if repair_dic[i] == t:
            repair_dic[i] = 0
            cnt += 1
            chc = True
        if repair_dic[i] < temp and repair_dic[i] != 0:
            temp = repair_dic[i]
    minV_2 = temp
    return chc

def put_repair(n, t):
    global minV_2, minX_2, M
    chc = False
    for i in range(M):
        # 자리가 있는경우
        if repair_dic[i] == 0 and not chc:
            rep[i].append(n)
            repair_dic[i] = t + repair[i]
            chc = True
        if minV_2 > repair_dic[i] and repair_dic[i] != 0:
            minV_2 = repair_dic[i]
            minX_2 = i
    # 가득 차있는경우
    if not chc:
        wait.append(n)
    return chc

T = int(input())
for t in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    receipt = list(map(int, input().split()))
    repair = list(map(int, input().split()))
    client = list(map(int, input().split()))
    rec = [[0] for _ in range(N)]
    rep = [[0] for _ in range(M)]
    wait = []
    receipt_dic = {}
    repair_dic = {}
    for i in range(N):
        receipt_dic[i] = (0, 0)
    for j in range(M):
        repair_dic[j] = 0
    # print(repair_dic)
    sec = client[0]
    top = 0
    cnt = 0
    while cnt < K:
        if sec == minV_2:
            if check_2(sec):
                if wait != []:
                    temp = []
                    for i in range(len(wait)):
                        if not put_repair(wait[i], sec):
                            temp.append(wait[i])
                    wait = temp
        if sec == minV:
            check(sec)
        if top < K and sec >= client[top]:
            for i in range(top, K):
                # print(client[i], i, top)
                if client[i] > sec:
                    break
                if top < K and put_receipt(i+1, sec):
                    top += 1
        # print(sec, receipt_dic, repair_dic, client, minV, minV_2, cnt, wait)
        # rs = sec
        # if top < K:
        #     sec = min(minV, minV_2, client[top])
        # else:
        #     sec = min(minV, minV_2)
        # if sec == 99999 or sec == rs:
        #     sec = rs + 1
        sec += 1
    # print(rec, rep)
    res = 0
    for i in rec[A-1]:
        for j in rep[B-1]:
            if i == j:
                res += i
                break
    if res == 0:
        res = -1
    print(f"#{t} {res}")