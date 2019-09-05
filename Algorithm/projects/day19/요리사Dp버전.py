# 1인 비트가 1개~8개까지인 숫자 저장
bitCnt = [[] for _ in range(9)]

for i in range(1, 1 << 16):
    cnt = 0
    for j in range(16):
        if i & (1 << j) != 0:
            cnt += 1
    if cnt <= 8:
        bitCnt[cnt].append(i)

# 문제 풀이 시작
T = int(input())
for tc in range(1, 2):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    synergy = [0] * (1 << N)

    # 재료가 2개인 경우 synergy 계산. x는 재료번호 비트가 1로 표시
    for x in bitCnt[2]:
        if x < (1 << N):
            one = []
            for i in range(N):
                if x & (1 << i) != 0:
                    one.append(i)

            synergy[x] = arr[one[0]][one[1]] + arr[one[1]][one[0]]

    # 재료가 3부터 N//2개 까지의 시너지 계산
    for y in range(3, N // 2 + 1):
        for x in bitCnt[y]:
            if x < (1 << N):  # 주어진 재료 개수 이내인 숫자의 비트 구성만 고르고
                for i in range(N):  # 첫번째 1인 비트를 찾고
                    if (x & (1 << i)) != 0:  # 해당 비트를 제외하고 나머지 재료의 시너지를 가져옴
                        first = i
                        break
                synergy[x] += synergy[~(1 << first) & x]
                for i in range(first + 1, N):
                    if (x & (1 << i)) != 0:
                        synergy[x] += synergy[(1 << first) | (1 << i)]
    # 재료가 N//2인 경우에 대해, A요리와  B요리 시너지 비교 (비트 구성이 반대)
    diff = []
    for x in bitCnt[N // 2]:
        if x < (1 << N):  # 사용되는 범위면
            diff.append(abs(synergy[x] - synergy[(1 << N) - 1 - x]))
    print('#{} {}'.format(tc, min(diff)))
