import sys

sys.stdin = open("input.txt", "r")

# 괄호 탐색 해당 괄호의 짝이 되는 괄호를
# stack에 넣어준다. 그리고 짝이 되는 괄호가 나오면 빼준다. 만약 틀리다면 break
for t in range(1, 11):
    N = int(input())
    word = input()
    stack = []
    check = False
    for i in word:
        if i == "(":
            stack.append(")")
        elif i == ")":
            if i != stack.pop():
                break
        elif i == "{":
            stack.append("}")
        elif i == "}":
            if i != stack.pop():
                break
        elif i == "[":
            stack.append("]")
        elif i == "]":
            if i != stack.pop():
                break
        elif i == "<":
            stack.append(">")
        elif i == ">":
            if i != stack.pop():
                break
    if stack == []:
        print(1)
    else:
        print(0)