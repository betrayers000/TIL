import sys

sys.stdin = open('sh.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # 즐거운 날의 수
    N = int(input())
    days = [int(input()) for x in range(N)]
    # 배의 수 세기
    cnt = 0
    # 배의 주기를 바꿔가면서 계속체크해야한다
    # 시작점은 아예 빼고 시작하고 간격체크한 값은 계속 빼버린다
    start = days.pop(0)
    # 간격별로 값들이 모이는 곳
    spot = []
    # 최소값을 구하기 위해서 설정
    # (total 1을 제외한 모든 숫자가 들어오면 모든배가 들어온것으로 생각)
    total = set()
    temp = set()
    while days:
        end = days[0]
        interval = abs(start - end)
        if not spot:
            check = start + interval
            total.add(check)
            if check in days:
                spot.append(check)
        elif spot:
            day = spot[-1]
            check = day + interval
            if check in days:
                spot.append(check)
                total.add(check)
            else:
                # print(total, temp)
                if temp != total:
                    cnt += 1
                temp = total.copy()
                # cnt += 1
                days.pop(0)
                if len(total) == N - 1:
                    break
                else:
                    spot = []
    print('#{} {}'.format(tc, cnt))
