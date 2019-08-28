import sys

sys.stdin = open('sky.txt', 'r')


for t in range(int(input())):
    # 가로줄과 세로줄을 모두 갖고 있는 size*2 짜리 리스트(mountain_status) 만들기
    size, length = map(int, input().split())
    mountain_status = [list(map(int, input().split())) for _ in range(size)]
    mountain_status += list(map(list, zip(*mountain_status)))
    # 각각의 줄에 대한 탐색 시작
    cnt = 0
    for line in mountain_status:
        # 기본적으로 가능하다 가정하고 탐색 시작
        impossible = False
        # 공사 여부 표시를 위해 index 와 0이나 1로 이루어진 리스트 indexes 를 생성
        # 1은 경사로가 깔리지 않은 땅이라는 의미 0은 경사로가 설치된 땅이라는 의미
        # 마지막 땅에서는 그 다음 땅과의 검사를 할 필요가 없기 때문에 -1 추가~
        indexes = [1] * size
        for index in range(size-1):
            this, that = line[index], line[index + 1]

            if this == that:
                continue
            else:
                toward_right = True
                # 다음 땅이 더 높다면 경사로를 왼쪽에 설치해야 한다
                if this < that:
                    # 지금 땅이 다음 땅보다 작으므로 왼쪽으로 탐색해야한다
                    toward_right = False
                # 경사 차이가 1보다 크면 활주로 건설이 불가능하다
                if abs(that - this) > 1:
                    impossible = True
                    break
                else:
                    for next in range(length):
                        # 다음 땅이 낮은 경우엔, 다음 땅부터 그 이후 땅들을 탐색
                        # 다음 땅이 높은 경우엔, 지금 땅부터 그 이전 땅들을 탐색
                        next_index = index + next + 1 if toward_right else index - next
                        # 탐색할 땅이 주어진 인덱스 값을 벗어난다면 건설 불가
                        # 탐색할 땅들에 활주로를 건설한 적이 있다면 건설 불가
                        if 0 > next_index or next_index >= size or indexes[next_index] != 1:
                            impossible = True
                            break
                        # 다음 땅이 낮은 경우엔, 다음 땅들의 높이가 모두 같아야..
                        # 다음 땅이 높은 경우엔, 지금 땅부터 그 이전 땅들의 높이가 같아야
                        if line[next_index] != that if toward_right else line[next_index] != this:
                            impossible = True
                            break
                    else:
                        for next in range(length):
                            next_index = index + next + 1 if toward_right else index - next
                            if 0 <= next_index < size:
                                indexes[next_index] = 0
                    if impossible:
                        break
        if not impossible:
            cnt += 1
    print("#{} {}".format(t + 1, cnt))