T = int(input())
for tc in range(1, T+1):
    # 원소의 수, 부분집합의 합
    N, K = map(int, input().split())
    # 집합 a생성
    A = [x for x in range(1, 13)]
    res = []
    for i in range(1<<12):
        pre=[]
        for j in range(12):
            if i & (1<<j):
                pre.append(A[j])
        res.append(pre)
    ans =0
    for part in res:
        if len(part) ==N:
            if sum(part) == K:
                ans += 1
    print("#{} {}".format(tc, ans))

