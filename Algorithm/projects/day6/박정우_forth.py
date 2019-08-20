def calc(stack, token):
    if len(stack) < 2:
        return stack, False
    s2 = stack.pop()
    s1 = stack.pop()
    if token == "+":
        stack.append(s1 + s2)
    elif token == "/":
        stack.append(int(s1 / s2))
    elif token == "*":
        stack.append(int(s1 * s2))
    elif token == "-":
        stack.append(s1 - s2)
    return stack, True

T = int(input())
for t in range(1, T+1):
    tokens = input().split()
    stack = []
    check = True
    for token in tokens:
        try:
            int(token)
            stack.append(int(token))
        except:
            if token == ".":
                break
            stack, check = calc(stack, token)
        if not check:
            break
    if check:
        if len(stack) > 1:
            print(f"#{t} error")
        else :
            print(f"#{t} {stack[-1]}")
    else :
        print(f"#{t} error")