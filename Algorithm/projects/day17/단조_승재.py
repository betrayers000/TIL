import sys

sys.stdin = open('test.txt', 'r')

for tc in range(int(input())):
    N = int(input())
    number = list(map(int, input().split()))
    result = []
    check = True
    for x in range(N - 1):
        for i in range(x + 1, N):
            a = str(number[x] * number[i])
            if len(a) == 1:
                result.append(int(a))
            elif len(a) > 1:
                for j in range(1, len(a)):
                    if int(a[j - 1]) > int(a[j]):
                        check = False
                        break
                if check:
                    result.append(int(a))
    result.sort()
    # print(result)
    print("#{} {}".format(tc + 1, result[-1]))
