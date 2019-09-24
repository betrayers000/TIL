# 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용
# 을 이렇게 풀어보세요.
#
# 물건을 주문하는 지역 좌표(i1, j1)와 각 공장의 위치 좌표(i2, j2)가 주어진다.
# 물건을 만드는 비용은 지역과 공장의 거리(|i1-i2|+|j1-j2|)로 결정된다면,
# 각 물건을 생산하는 최소 비용은 얼마인가? 한 공장에서 한 개의 물건만
# 생산한다.
# N과 N개의 지역 좌표, N개 공장의 좌표가 차례로 주어진다.
# (3<=N<=7,  -100<=i, j<=100)
# 3
# -24	-3
# -59	5
# -2	-79
# 25	-15
# -15	71
# -99	-92
def get_dis(i, j):
    x, y = location[i]
    x1, y1 = factory[j]
    return abs(x-x1) + abs(y-y1)


def f(n, k, s):
    global N, minV
    if n == k:
        if minV > s:
            minV = s
        return
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                p[n] = i
                f(n + 1, k, get_dis(n, i) + s)
                used[i] = 0

N = int(input())
location = [list(map(int, input().split())) for _ in range(N)]
factory = [list(map(int, input().split())) for _ in range(N)]
used = [0] * N
p = [0] * N
minV = 99999999
f(0, N, 0)
print(minV)