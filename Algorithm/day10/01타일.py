import sys
sys.setrecursionlimit(1000010)

def get_card(N):
    global memo

    if memo[N] == 0:
        memo[N] = get_card(N-1) + get_card(N-2)
        return memo[N]
    else:
        return memo[N]


memo = [0] * 1000000
memo[1] = 1
memo[2] = 2
for i in range(1, 1000000):
    get_card(i)

# total = 0
# n = 99999
# stack = [n]
# while 1:
#     if stack == []:
#         break
#     N = stack.pop()
#     if memo[N] == 0:
#         stack.append(N-1)
#         stack.append(N-2)
#     else:
#         total += memo[N]

