import sys

sys.stdin = open('math.txt', 'r')

p1 = [1, 2, 3, 4, 5]
p2 = [2, 1, 2, 3, 2, 4, 2, 5]
p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

T = int(input())
for t in range(1, T + 1):
    answers = list(map(int, input().split()))
    score = [0] * 3
    for i in range(len(answers)):
        if answers[i] == p1[i%5]:
            score[0] += 1
        if answers[i] == p2[i%8]:
            score[1] += 1
        if answers[i] == p3[i%10]:
            score[2] += 1
    maxV = max(score)
    ans = []
    for s in score:
        if maxV == s:
            ans.append(s)

    print(ans)




