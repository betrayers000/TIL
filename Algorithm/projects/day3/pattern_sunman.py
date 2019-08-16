for t in range(int(input())):
    ans = 0
    # 1
    N = input()
    M = input()
    size_N = len(N)
    size_M = len(M)
    # 2
    index_list = {}
    for index, value in enumerate(reversed(N[:-1])):
        if index_list.get(value) != None:
            continue
        else:
            index_list[value] = index+1
    start = 0
    while True:
        # 3
        print(start)
        if start + size_N > size_M:
            break
        else:
            # 4
            if N == M[start:start + size_N]:
                ans = 1
                start += size_N
            # 5
            else:
                if index_list.get(M[start + size_N-1]) == None:
                    start += size_N
                else:
                    start += index_list[M[start + size_N-1]]
    print(ans)