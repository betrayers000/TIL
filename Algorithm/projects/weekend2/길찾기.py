import sys

sys.stdin = open("input.txt", "r")

for t in range(1, 11):
    tc, N = map(int, input().split())
    line_list = []
    # 이전에 배운 x 인덱스 y 원소 방법을 사용
    # 최대 노드수가 100개이기 때문에 일단 100개의 리스트를 가진 리스틀 만든다
    for i in range(100):
        line_list += [[]].copy()
    line = list(map(int, input().split()))
    x = 0
    # 주어진 루트를 x, y값을 잘 넣는다.
    # 여기서는 2개씩 묶어서 나와서 인덱스가 홀수일경우 x값 아닐경우 y값으로 한다.
    for n in range(N*2):
        if not n % 2:
            x = line[n]
        else:
            line_list[x].append(line[n])
    # start와 end값을 초기화 해준다
    # stack을 start로 초기화해준다
    start = 0
    end = 99
    stack = [start]
    while True:
        # 종료조건 end에 도착했을때, stack 이 전부 비었을때
        if start == end:
            break
        # line_list[start]에서 가져온 값은 다음에 갈곳, 만약에 다음에 갈곳이 없으면
        # stack으로 돌아가서 찾는다.
        # pop을 이용함으로써 중복루트로 들어가지 않게 한다.
        # start를 이용해 진행하면(line_list[start].pop()이 오류없다면)
        # stack에 start를 넣어줌으로써 중간 지점을 기억한다.
        if line_list[start] == []:
            if stack == []:
                break
            start = stack.pop()
        try:
            start = line_list[start].pop()
        except:
            continue
        stack.append(start)
    # start가 99면 도착했기 때문에 1 아닐경우에는 도착하지 못해서 0 출력
    if start == 99:
        print(f"{tc} {1}")
    else:
        print(f"{tc} {0}")

