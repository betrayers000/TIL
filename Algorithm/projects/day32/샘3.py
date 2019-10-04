import sys

sys.stdin = open('sam3.txt', 'r')

for t in range(1, 2):
    input()
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 999999
    minH = 0
    for h in range(1, 30):
        for r in range(N):
            row = arr[r]
            for col in zip(*arr):
                val = 0
                for i in range(N):
                    val += abs(row[i] - h)
                    val += abs(col[i] - h)
                val -= abs(col[r] - h)
                if minV > val:
                    minV = val
                    minH = h
    print(minV, minH)