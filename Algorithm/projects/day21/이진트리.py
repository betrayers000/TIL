import sys

sys.stdin = open('input.txt', 'r')


# def f(n):
#     global result
#     if n > 0:
#         f(left[n])
#         result.append(n)
#         f(right[n])

def inorder(n, last):
    global cnt
    if n <= last:  # 유효한 노드이면 노드는 N까지만 존재한다.
        inorder(n * 2, last)  # 왼쪽 자식 노드
        tree[n] = cnt
        cnt += 1
        inorder(n * 2 + 1, last)  # 오른쪽 자식노드


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    cnt = 1
    inorder(1, N)
    print(tree[1], tree[N // 2])
    # left = [0] * (N + 1)
    # right = [0] * (N + 1)
    # idx = 1
    # for i in range(2, N + 1, 2):
    #     left[idx] = i
    #     if i + 1 <= N:
    #         right[idx] = i + 1
    #     idx += 1
    # result = []
    # f(1)
    # rot = result.index(1) + 1
    # z = result.index(N // 2) + 1
    # print(rot, z)
