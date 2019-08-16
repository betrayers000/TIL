import sys

sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    N = int(input())
    calc = [input().split() for n in range(N)]
    size = len(calc)
    cnt = 0
    for c in calc:
        for a in c:
            try:
                int(a)
            except:
                cnt += 1
    nums = []
    sig = []
    for ca in calc[::-1]:
        if len(ca) == 2:
            try:
                nums.append(int(ca[1]))
            except:
                sig.append(ca[1])
        else:
            break
    if sig == []:
        print(1)
    else:
        print(0)

