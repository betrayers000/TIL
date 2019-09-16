import sys

sys.stdin = open('code.txt', 'r')

history = []
history_2 = []

def get_code(code, N, M):
    global history
    f = []
    for i in range(N):
        if code[i].count('0') != M:
            # history에 넣어서 동일한 문장은 검사하지않는다.
            if code[i] not in history:
                history.append(code[i])
                b_code = change_binary(code[i])
                while 1:
                    c_code = cut_code(b_code)
                    b_code = c_code
                    if c_code == '0':
                        break
                    p = 1
                    while 1:
                        t, result, cc = scan_code(c_code, p)
                        if t:
                            break
                        p += 1
                    # 반환된 코드를 계산하여 올바른 코드인지 확인
                    a1, a2 = 0, 0
                    if result not in history_2:
                        history_2.append(result)
                        for i in range(len(result[:-1])):
                            if i % 2:
                                a1 += result[i]
                            else:
                                a2 += result[i]
                        a = a1 + a2 * 3
                        if (a + result[-1]) % 10 == 0:
                            f.append(sum(result))
                    # 한 줄에 여러 코드가 있는경우 검사한 코드의 경우
                    # cc로 반환을 받고 해당 코드를 replace로 삭제한다.
                    b_code = b_code.replace(cc, "")
    return f


def change_binary(code):
    # 16진수를 2진수로 변환해준다.
    a = ['A', 'B', 'C', 'D', 'E', 'F']
    code = list(code)
    M = len(code)
    for i in range(M):
        if code[i] in a:
            code[i] = a.index(code[i]) + 10
        else:
            code[i] = int(code[i])
    temp = ''
    for i in range(M):
        for j in range(3, -1, -1):
            if code[i] & (1 << j):
                temp += '1'
            else:
                temp += '0'
    return temp

def cut_code(temp):
    # 뒤에 0을 삭제해준다.
    last_idx = 0
    for j in range(len(temp) - 1, -1, -1):
        if temp[j] == '1':
            last_idx = j
            break
    return temp[0:last_idx + 1]



def scan_code(code, p):
    # 코드를 스캔한다.
    # p는 배율
    global list_idx
    idx = [0] * 4
    code = code[-p * 56:]
    # 배율만큼 코드를 잘라낸다.
    n = len(code)
    temp = '1'
    cnt = 0
    z = 3
    change = []
    k = 0
    # change는 변환 코드를 담는 리스트
    # temp는 비교군 1로 시작하기때문에 1을 초기값으로 준다.
    # z는 idx 인덱스 값 뒤에서 부터 읽기때문에 3으로 시작하고 0으로 끝난다.
    # cnt는 0과 1의 카운트
    # k는 배율에 맞게 코드한개의 개수를 체크한다.
    for i in range(n - 1, -1, -1):
        k += 1
        # temp와 코드가 같으면 cnt를 올리고
        # 다르면 cnt // p 만큼의 값을 idx에 넣어준다.
        if temp == code[i]:
            cnt += 1
        else:
            temp = code[i]
            idx[z] = cnt // p
            cnt = 1
            z -= 1
        # 한 코드값의 종료조건
        # k가 7*p의 값이면 마지막 코드이기때문에
        # 지금까지 카운팅한 값을 idx[0] 값에 넣어준다.
        # 이 상황에서 만약 코드가 틀린 코드인 경우 false를 돌려준다.
        # false를 반환하게 되면 p를 증가시켜서 다시 검사한다.
        # 마지막 0이 앞으로 많이 붙기 때문에 그경우에 true 반환
        if k == 7 * p:
            idx[0] = cnt // p
            if len(change) >= 1 and idx.count(0) >= 1:
                return True, change[::-1], code
            if idx not in list_idx or idx.count(0) >= 1:
                return False, [], ''
        if idx[0] != 0:
            if idx not in list_idx:
                return False, [], ''
            change.append(list_idx.index(idx))
            # 초기화
            idx = [0] * 4
            z = 3
            k = 0
            cnt = 0
            temp = code[i - 1]
    return True, change[::-1], code


list_idx = [
    [3, 2, 1, 1],
    [2, 2, 2, 1],
    [2, 1, 2, 2],
    [1, 4, 1, 1],
    [1, 1, 3, 2],
    [1, 2, 3, 1],
    [1, 1, 1, 4],
    [1, 3, 1, 2],
    [1, 2, 1, 3],
    [3, 1, 1, 2]
]
T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]
    result = get_code(code, N, M)
    if result == []:
        result = 0
    else:
        result = sum(result)
    print("#{} {}".format(t, result))
