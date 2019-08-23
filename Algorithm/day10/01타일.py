import sys
sys.setrecursionlimit(1000010)

# def get_card(N):
#     global memo
#
#     if memo[N] == 0:
#         memo[N] = get_card(N-1) + get_card(N-2)
#         return memo[N]
#     else:
#         return memo[N]
#

memo = [0] * 1000010
memo[1] = 1
memo[2] = 2
N = 1000000
for i in range(1, N+1):
    if memo[i] == 0:
        memo[i] = (memo[i-1]%15746) + (memo[i-2]%15746)
print(memo[N])

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

