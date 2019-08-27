import sys

sys.stdin = open('switch.txt', 'r')

N = int(input())
switch = list(map(int, input().split()))
M = int(input())
for m in range(M):
    a, b = list(map(int, input().split()))
    if a == 1:
        for i in range(1, N+1):
            if i % (b) == 0:
                switch[i-1] = abs(switch[i-1] - 1)
    elif a == 2:
        switch[b-1] = abs(switch[b-1] - 1)
        li = b - 2
        ri = b
        while li >= 0 and ri < N and switch[li] == switch[ri]:
            switch[li] = abs(switch[li] - 1)
            switch[ri] = abs(switch[ri] - 1)
            li -= 1
            ri += 1

while switch != []:
    if len(switch) > 20:
        print(" ".join(map(str, switch[:20])))
        switch = switch[20:]
    else:
        print(" ".join(map(str, switch)))
        switch = []