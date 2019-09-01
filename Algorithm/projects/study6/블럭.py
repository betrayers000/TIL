import sys

sys.stdin = open('block.txt', 'r')

T = int(input())
f = []
for t in range(1, T + 1):
    N = int(input())
    block = list(map(int, input().split()))
    ans = sum(block)
    cnt = 0
    total = 0
    while 1:
        next_ = []
        b1 = 0
        for i in range(len(block)):
            now = block[i]
            if i + 1 < len(block):
                b3 = block[i + 1]
            else:
                b3 = 0
            if now == 0:
                continue
            s = b1 if b1 < b3 else b3
            if now <= s:
                m = 1
            else:
                m = now - s
            next_.append(now - m)
            total += m
            b1 = now
        block = next_
        cnt += 1
        if total == ans:
            break
    print(f"Case #{t}\n{cnt}")
