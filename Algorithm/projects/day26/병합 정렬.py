import sys

sys.stdin = open('quick.txt', 'r')


T = int(input())
for t in range(1, T+1):
    cnt = 0
    N = int(input())
    arr = list(map(int, input().split()))
    nrr = []
    for i in range(N):
        nrr.append([arr[i]])
    print(nrr)

