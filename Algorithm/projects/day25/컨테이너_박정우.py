import sys

sys.stdin = open('contain.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    tr = list(map(int, input().split()))
    w = sorted(w, reverse=True)
    total = 0
    for i in tr:
        for j in w:
            if i >= j:
                total += j
                w.remove(j)
                break
    print(total)