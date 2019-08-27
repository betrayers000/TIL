import sys

sys.stdin = open('stick.txt', 'r')

stick = input()

stack = []
sticks = []
razer = []
# for idx, val in enumerate(stick):
#     if val == "(":
#         stack.append(idx)
#     elif val == ")":
#         dx = stack.pop()
#         if idx-dx == 1:
#             razer.append(idx)
#         else:
#             sticks.append([dx, idx])
# total = 0
# for stick in sticks:
#     cnt = 0
#     for i in range(stick[0], stick[1]):
#         if i in razer:
#             cnt+= 1
#     total += cnt+1
# print(total)

stick = stick.replace("()", "0")
cnt = 0
for i in stick:
    if i == ")":
        stack.pop()
        cnt += 1
    elif i == "(":
        stack.append(i)
    else:
        cnt += len(stack)
print(cnt)