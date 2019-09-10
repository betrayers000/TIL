import sys

sys.stdin = open('inorder.txt', 'r')

def inorder(n):
    global N
    if n <= N:
        inorder(n*2)
        result.append(tree[n])
        inorder(n*2+1)


for t in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    result = []
    for _ in range(N):
        node = input().split()
        tree[int(node[0])] = node[1]
    inorder(1)
    print(''.join(result))
