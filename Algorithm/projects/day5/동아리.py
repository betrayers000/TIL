import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    member = ["A", "B", "C", "D"]
    code = list(input())
    result = []
    for i in range(1<<4):
        temp = []
        for j in range(4):
            if i & (1<<j):
                temp.append(member[j])
        result.append("".join(temp))
    stack = []
    for s in code:
        # 1일차
        if stack == []:
            temp = []
            for r in result:
                if s in r and "A" in r:
                    temp.append(r)
            stack.append(temp)
        # 2일차 이후
        else:
            yd_member = stack.pop()
            temp = []
            for y in yd_member:
                temp_ = set()
                for z in y:
                    for r in result:
                        if z in r and s in r:
                            temp_.add(r)
                temp.extend(list(temp_))
            stack.append(temp)
    total = 0
    for i in stack[-1]:
        total += 1

    print(total)










