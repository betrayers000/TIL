import sys

sys.stdin = open('room.txt', 'r')

def turn(room, n):
    global N
    for i in range(N):
        if i < N and (i+1)%n == 0:
            room[i] = abs(room[i] -1)
    return room


T = int(input())
for t in range(1, T+1):
    N = int(input())
    room = list(map(int, input().split()))
    z = [0] * N
    cnt = 0
    while room != z:
        for i in range(N):
            if room[i] == 1:
                room = turn(room, i+1)
                break
        cnt += 1
    print(cnt)
