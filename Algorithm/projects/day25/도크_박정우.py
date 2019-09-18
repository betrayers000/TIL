import sys

sys.stdin = open('dok.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    time = [0] * 25
    cnt = 0
    tr = [list(map(int, input().split())) for _ in range(N)]
    tr = sorted(tr, key=lambda x:abs(x[1]-x[0]))
    for _ in range(N):
        start, end = tr[_]
        temp = time.copy()
        for i in range(start, end):
            if time[i] == 1:
                time = temp
                break
            time[i] = 1
        else:
            cnt += 1
    print(cnt)