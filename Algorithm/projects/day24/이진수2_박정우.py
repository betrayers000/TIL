import sys

sys.stdin = open('binary.txt', 'r')


T = int(input())
for t in range(1, T+1):
    N = float(input())
    index = [0] * 13
    check = False
    result = ''
    for i in range(1<<13):
        if check:
            break
        b = ""
        for j in range(13):
            if i&(1<<j):
                b+= '1'
            else:
                b+= '0'
        total = 0
        for k in range(len(b)):
            total += float(int(b[k]) / (1<<(k+1)))
            if total == N:
                check = True
                result += b
                break
    if check:
        lastidx = 0
        for i in range(13):
            if result[i] == '1':
                lastidx = i+1
        print(f"#{t} {result[:lastidx]}")
    else:
        print(f"#{t} overflow")
