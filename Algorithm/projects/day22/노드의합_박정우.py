import sys

sys.stdin = open('nodesum.txt', 'r')

def f(n):
    global N
    if heap[n] == 0:
        a, b = 0, 0
        if n*2 <= N:
            a = f(n*2)
        if n*2+1 <= N:
            b = f(n*2+1)
        heap[n] = a+b
        return heap[n]
    else:
        return heap[n]



T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    heap = [0] * (N+1)
    for _ in range(M):
        idx, val = map(int, input().split())
        heap[idx] = val
    f(1)
    print(heap[L])
