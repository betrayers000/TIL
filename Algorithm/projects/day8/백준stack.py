

def stack_func(c1, c2):
    global stack
    if c1 == "push":
        stack.append(c2)
        return -2
    elif c1 == "top":
        if stack == []:
            return -1
        return stack[-1]
    elif c1 == "size":
        return len(stack)
    elif c1 == "empty":
        if stack == []:
            return 1
        else:
            return 0
    elif c1 == "pop":
        if stack == []:
            return -1
        else:
            result = stack[-1]
            stack = stack[:-1]
            return result


T = int(input())
stack = []
f = []
for t in range(1, T+1):
    command = input().split()
    c2 = 0
    if len(command) == 2:
        c1 = command[0]
        c2 = command[1]
    else:
        c1 = command[0]
    result = stack_func(c1, c2)
    if result == -2:
        continue
    else:
        f.append(str(result))
print("\n".join(f))

