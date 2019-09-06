import sys

sys.stdin = open('test.txt', 'r')

T = int(input())
for t in range(1, 2):
    N = int(input())
    score = [0] + list(map(int, input().split()))
    dp = [0] * (sum(score) + 1)
    dp[0] = True
    cnt = 1
    for i in range(N + 1):
        for j in range(10, -1, -1):
            if dp[j]:
                if not dp[score[i] + j]:
                    dp[score[i] + j] = True
                    cnt += 1

    print(cnt)
