import sys

sys.stdin = open('graph.txt', 'r')

# def dfs(n):
#     global V
#     print(n)
#     visited[n] = 1
#     for i in range(1, V + 1):
#         if adj[n][i] == 1 and visited[i] == 0:
#             dfs(i)
#
#
# def dfs2(n, k):
#     global V
#     if n == k:
#         print(n)
#         return 1
#     else:
#         visited[n] = 1
#         for i in range(1, V + 1):
#             if adj[n][i] == 1 and visited[i] == 0:
#                 if dfs2(i, k) == 1:
#                     return 1
#         return 0

def dfs_(n, V):
    stack = [0] * V
    top = -1
    top += 1
    stack[top] = n
    visited[n] = 1
    while top >= 0:
        n = stack[top]
        top -= 1
        print(n)
        for i in range(1, V+1):
            if adj[n][i] == 1 and visited[i] == 0:
                top += 1
                stack[top] = i
                visited[i] = 1






V, E = map(int, input().split())
adj = [[0] * (V + 1) for _ in range(V + 1)]
edge = list(map(int, input().split()))
visited = [0] * (V + 1)
for i in range(E):
    n1, n2 = edge[i * 2], edge[i * 2 + 1]
    adj[n1][n2] = 1
    # 방향성이 있을때는 이걸 빼줘야 한다.
    # adj[n2][n1] = 1
# dfs(4)
# print(dfs2(4, 3))
dfs_(1, V)
print(visited)
