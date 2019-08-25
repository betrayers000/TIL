T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    goods = [list(map(int, input().split())) for n in range(N)]
    index_list = list(range(N))


    max_c = 0
    for i in range(1<<N):
        v_total = 0
        c_total = 0
        for j in range(N):
            if i & (1<<j):
                v = goods[index_list[j]][0]
                c = goods[index_list[j]][1]
                v_total += v
                if v_total > K:
                    break
                else:
                    c_total += c
        if max_c < c_total:
            max_c = c_total

    print(max_c)

