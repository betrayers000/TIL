import sys

sys.stdin = open('card.txt', 'r')


def npr(n, k, m):
    global res
    if n == k:
        res.append(p.copy())
    else:
        for l in range(m):
            p[n] = l
            npr(n+1, k, m)

TC = int(input())
for t in range(TC):
    N = int(input()) # 카드 개수
    cards = list(map(int, input().split())) # N개의 정수들

    res = [] # 0~N-1까지 모든 숫자들 순열
    for k in range(1, 6): # 5회이므로 5개까지...본다
        p = [0] * k
        npr(0, k, N)

    cnt = -1

    for i in range(len(res)):
        left = cards[:N // 2][::-1]  # 왼쪽 덱
        right = [0] * (N // 2) + cards[N // 2:][::-1]  # 오른쪽 덱

        for j in range(len(res[i])):
            x = res[i][j]

            left_posible = [0]
            for q in range(len(left)):
                left_posible += [left[q]] + [0]  # 0 1 0 2 0 1 0 0 0 0 0과 같이 들어갈 자리 만들어줌

            left_posible += [0] * 10

            for z in range(x + 1):
                left_posible[2 * z] = right[-(x+1) + z]  # left_posible의 0 자리에 넣어준다.

            for l in range(left_posible.count(0)):  # left_posible에 남은 0을 제외한다.
                left_posible.remove(0)

            marge = right[-len(right):-(x+1)] + left_posible  # right에 있는 남은 0을 제외한다.
            for l in range(marge.count(0)):
                marge.remove(0)

            left = marge[:N//2][::-1]
            right = [0] * (N // 2) + marge[N//2:][::-1]
            if marge == sorted(cards) or marge == sorted(cards)[::-1]:  # marge가 오름차순이거나 내림차순이면 성공
                cnt = len(res[i])
                break
        if cnt != -1:
            break
    if cnt == -1:
        print('#{} -1'.format(t+1))
    else:
        print('#{} {}'.format(t+1, cnt))