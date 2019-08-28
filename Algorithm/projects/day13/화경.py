import sys

sys.stdin = open('sky.txt', 'r')


def air(n, x, airstrip):
    result = 0
    for i in range(n):
        if type(airstrip[i]) != list:
            airstrip[i] = list(airstrip[i])
        count = 0
        strip = [0] + airstrip[i] + [0]
        max_num = max(strip)
        check = True
        for j in range(1, n):
            if strip[j] != max_num:
                for r in range(x-1):
                    print(strip[j+r], strip[j+1+r])
                    if strip[j + r] != strip[j + 1 + r]:
                        check = False
                        break
            if not check:
                break
        else:
            if check:
                count += 1
        if count > 0:
            print(airstrip[i])
            result += 1
    return result

int(input())
for tc in range(1):
    n, x = map(int, input().split())
    airstrip = [list(map(int, input().split())) for _ in range(n)]
    airstrip_row = list(zip(*airstrip))
    print(air(n, x, airstrip) + air(n, x, airstrip_row))
