import sys

sys.stdin = open('bank.txt', 'r')

def f(n, b, c):
    global nums, result
    # 첫 계산시 -1을 넣어서 계산한다. 한자리만 바꾸면 되기 때문
    if n != -1:
        total = 0
        for i in range(len(b)):
            total += b[i] * (len(c)**(len(b)-i-1))
        if total in nums:
            result = total
        nums.append(total)
        return
    else:
        # 자리를 바꿔준다 i는 바꿔줘야할 인덱스
        # j는 바꿔서 넣어줘야 할 숫자의 인덱스
        for i in range(len(b)):
            # 원상복구 하기 위해서 temp에 넣어서 복구를 위해 준비한다.
            temp = b[i]
            for j in range(len(c)):
                if c[j] != temp:
                    b[i] = c[j]
                    f(i, b, c)
                    # 재귀가 끝나면 다시 원상복구해줘야한다.
                    b[i] = temp

T = int(input())
b_ = [0, 1]
c_ = [0, 1, 2]
for t in range(1, T+1):
    nums = []
    result = 0
    b = list(map(int, list(input())))
    c = list(map(int, list(input())))
    f(-1, b, b_)
    f(-1, c, c_)
    print(result)