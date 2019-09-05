import sys

sys.stdin = open('room.txt', 'r')

def search_room(num):
    global room

    for i in range(200):
        a, b = room[i]
        if a == num or b == num:
            return i

def check_overlap(temp):
    sample = [0] * 200
    for t in temp:
        for i in t:
            sample[i] += 1
    return max(sample)

T = int(input())
room = [0] * 200
for i in range(200):
    room[i] = [i*2+1, i*2+2]
for t in range(1, T+1):
    N = int(input()) # 학생수
    path = [list(map(int, input().split())) for _ in range(N)] # 현재방, 돌아갈 방
    temp = [0] * N
    for i in range(N):
        start, end = path[i]
        a = max(search_room(start), search_room(end))
        b = min(search_room(start), search_room(end))
        temp[i] = list(range(b, a+1))
    print("#{} {}".format(t, check_overlap(temp)))