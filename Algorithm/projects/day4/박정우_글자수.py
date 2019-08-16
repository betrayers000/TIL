T = int(input())
for t in range(1, T + 1):
    search = input()
    words = input()
    mxcount = 0
    for s in search:
        count = 0
        for w in words:
            if s == w:
                count += 1
        if mxcount < count:
            mxcount = count
    print(mxcount)

