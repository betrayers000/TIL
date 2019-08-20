import sys

sys.stdin = open('input.txt', 'r')

def cyclefire(pizza):
    # 피자 화덕을 한바퀴 돌린다.
    # i[1] 을 //2 해준다.
    result = []
    for i in pizza:
        result.append((i[0], i[1]//2))
    return result

def count_in(in_):
    # 0을 카운트해준다.
    cnt = 0
    for i in in_:
        if i[1] == 0:
            cnt += 1
    return cnt



T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    # 피자 번호랑 치즈 수를 튜플 형태로 저장한다.
    pizza = list(enumerate((map(int, input().split()))))
    print(pizza)
    in_ = [(0, 0)]*N
    # 앞에서부터 화덕안에 피자를 채워넣는다
    for i in range(N):
            in_[i] = pizza.pop(0)
    # queue = [[f]]
    cycle = 0
    while True:
        # in_ = queue[cycle].pop()
        if pizza == []:
            cnt = count_in(in_)
            # 피자 0의 갯수를 새어서 N과 같으면 모두 돌아갔다.
            # 결과값을 리턴한다.
            if cnt == N:
                result = in_
                break
        for j in range(N):
            # 화덕정보를 확인해서 0인 경우 다음 피자로 교환해준다.
            # 피자가 없을때에는 -1, 0 을 넣어준다.
            if in_[j][1] == 0:
                if pizza  != []:
                    in_[j] = pizza.pop(0)
                else :
                    in_[j] = (-1, 0)
        # 피자 화덕을 돌린 정보를 in_에 저장한다
        in_ = cyclefire(in_)

        # after_ = cyclefire(in_)
        # cycle += 1
        # queue += [[]].copy()
        # queue[cycle].append(after_)

    z = 0
    # 리턴값을 가지고 피자 인덱스가 -1이 아닌 수를 구한다. 그게 마지막에 남은 피자이다.
    # 1번입구에서 꺼낼수 있으니 맨 마지막 피자가 마지막에 나온다.
    for r in result:
        if r[0] != -1:
            z = r[0]
    print(z+1)




