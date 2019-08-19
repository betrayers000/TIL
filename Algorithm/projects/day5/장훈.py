import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    lens = list(map(int, input().split()))
    result = []
    for i in range(1<<N):
        temp = []
        for j in range(N):
            if i & (1<<j):
                temp.append(lens[j])
        top = sum(temp)
        if top >= B:
            result.append(top)
    print(min(result)-B)