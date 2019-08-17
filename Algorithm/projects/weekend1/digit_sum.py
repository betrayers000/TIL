import sys

sys.stdin = open("input.txt", "r")
# 결과값을 밖으로 저장해서 print 한번만 사용해야한다.
T = int(input())
for t in range(1, T+1):
    n = input()
    while True:
        if len(n) < 2:
            break
        total = 0
        for i in range(len(n)):
            total += int(n[i])
        n = str(total)

    print(n)