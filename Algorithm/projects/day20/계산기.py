import sys

sys.stdin = open('calc.txt', 'r')

def f(n, k, m, s):
    global N, nums, used, temp
    if int(s) > N:
        return
    if n == m:
        if int(s) != 0:
            if N%int(s) == 0:
                print(s)
                temp.append(int(s))
        return
    else:
        for i in range(k):
            p[n] = nums[i]
            f(n+1, k, m, s+str(nums[i]))

def check(a):
    global sub
    for i in range(len(sub)):
        for j in sub[i]:
            if a == j:
                return j
    return -1


T = int(input())
for t in range(1, 2):
    state = list(map(int, input().split()))
    N = int(input())
    nums = []
    for i in range(10):
        if state[i] == 1:
            nums.append(i)
    sub = [[]] * (len(str(N)) + 1)
    for i in range(1, len(str(N))+1):
        p = [0] * i
        temp = []
        f(0, len(nums), i, "0")
        if temp != []:
            sub[i-1] = temp
    print(sub)
    s_list = []
    for i in range(len(sub)):
        for x in sub[i]:
            s_list.append(x)
    # q = []
    # q.append(N)
    # chk = True
    # result = []
    # d = len(q)
    # ic = 0
    # cnt = 0
    # if s_list == [1]:
    #     print(-1)
    #     continue
    # while chk:
    #     start = q.pop(0)
    #     for n in s_list:
    #         a = start//n
    #         b = check(a)
    #         if b == -1:
    #             q.append(a)
    #         else:
    #             result.append(len(str(n)) + len(str(b)))
    #             chk = False
    #     ic += 1
    #     if d == ic:
    #         d = len(q)
    #         ic = 0
    #         cnt += 1
    # print(min(result) + cnt)










