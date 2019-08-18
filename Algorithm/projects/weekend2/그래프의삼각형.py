import sys

sys.stdin = open("input.txt", "r")

T = int(input())
f = []
for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    # point 좌표를 기록할 리스트를만든다
    # 좌표기록은 x좌표가 인덱스 번호, y좌표가 해당인덱스에 포함되어있는 숫자이다.
    # 만들때 주석처리된 방식으로 만들면 런타임오류가 뜸
    # point = [[] for m in range(M+1)]
    point = []
    for i in range(N+1):
        point += [[]].copy()
    tri = 0
    for n in range(M):
        x, y = map(int, input().split())
        point[x].append(y)
    print(point)

    # 만들어진 리스트를 가지고 비교를 한다.
    # x = 1부터 비교를 시작하며
    # 1일때 해당 인덱스 내에 2와 3이 있으면, 2번 인덱스에 3이있을시에 삼각형이 성립된다.
    # 이를 반복한다.
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if j in point[i]:
                for k in range(j+1, N+1):
                    if k in point[i]:
                        if k in point[j]:
                            tri += 1
    print(tri)

