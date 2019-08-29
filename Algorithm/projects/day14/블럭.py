import sys

sys.stdin = open('block.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    block = [0] + list(map(int, input().split())) + [0]
    ans = sum(block)
    cnt = 0
    total = 0
    while 1:
        next_ = [0] * (N + 2)
        for i in range(1, N + 1):
            b1, now, b3 = block[i - 1], block[i], block[i + 1]
            if now == 0:
                continue
            if b1 < b3:
                s = b1
            else:
                s = b3
            if now <= s:
                m = 1
            else:
                m = now - s
            next_[i] = now - m
            total += m
        block = next_
        cnt += 1
        if total == ans:
            break

    # print(f"Case #{t}")
    print(cnt)
