import sys

sys.stdin = open('baby.txt', 'r')


def check(m):
    cnt = 0
    for j in range(10):
        if m[j] > 0:
            cnt += 1
        else:
            cnt = 0
        if m[j] > 2 or cnt > 2:
            return True
    return False


T = int(input())
for t in range(1, T + 1):
    card = list(map(int, input().split()))
    left, right = [0] * 10, [0] * 10
    res = 0
    for i in range(0, 12, 2):
        right[card[i + 1]] += 1
        left[card[i]] += 1
        if check(left) and check(right):
            res = 1
            break
        elif check(left) and not check(right):
            res = 1
            break
        elif not check(left) and check(right):
            res = 2
            break
    print("#{} {}".format(t, res))
