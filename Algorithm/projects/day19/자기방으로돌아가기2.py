import sys

sys.stdin = open('room.txt', 'r')

T = int(input())
for t in range(1, 2):
    N = int(input())  # 학생수
    path = [list(map(int, input().split())) for _ in range(N)]  # 현재방, 돌아갈 방
    comp = [0] * N
    cnt = 0
    while 0 in comp:
        room = [0] * 201
        for i in range(N):
            if comp[i] == 0:
                a, b = path[i]
                if a % 2:
                    a += 1
                if b % 2:
                    b += 1
                start = min(a//2, b//2)
                end = max(a//2, b//2)
                for j in range(start, end+1):
                    if room[j] != 0:
                        break
                else:
                    room[start:end+1] = [1] * (end-start+1)
                    comp[i] = 1
        cnt += 1
        print(room)
    print(cnt)
    room = [0] * 201
    for i in range(N):
        a, b = path[i]
        if a % 2:
            a += 1
        if b % 2:
            b += 1
        start = min(a // 2, b // 2)
        end = max(a // 2, b // 2)
        for j in range(start, end + 1):
             room[j] += 1
    print(room)
    print(max(room))
