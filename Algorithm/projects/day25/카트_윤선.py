import sys

sys.stdin = open('cart.txt', 'r')


def findM(start, arrive, val, k, used):
    global minE, N
    if val > minE:
        return
    if k == N:
        if minE > val + arr[arrive][0]:
            minE = val + arr[arrive][0]
        return
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                findM(arrive, i, val + arr[arrive][i], k + 1, used)
                used[i] = 0


for t in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minE = 100 * (N+1)
    # for i in range(1, N):
    #     findM(0, i, arr[0][i], 1, [1] + [0] * (N - 1))
    # 이렇게 넣어주면 중복 하는 경우가 있고 그 경우에서 오답이 나오는듯함
    # 항상 시작은 0이기 때문에 재귀 들어가서 다음 지점 받아서 바로 더하면
    # 되기 때문에 그냥 이렇게 써주기만 해도 됨
    findM(0, 0, 0, 1, [1] + [0] * (N - 1))
    print('#' + str(t + 1), minE)
