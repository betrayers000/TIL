T = int(input())
for t in range(1, T+1):
    code = input()
    temp = []
    for c in code:
        if c == '(':
            temp.append(')')
        elif c == '{':
            temp.append('}')
        elif c == ')':
            if temp != [] and temp[-1] == c:
                temp.pop()
            else:
                temp.append(c)
                break
        elif c == '}':
            if temp != [] and temp[-1] == c:
                temp.pop()
            else:
                temp.append(c)
                break
    if temp == []:
        result = 1
    else :
        result = 0
    print(f"#{t} {result}")