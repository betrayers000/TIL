import sys

sys.stdin = open('heap.txt', 'r')

def f(n):
    if n > 0:
        if heap[n//2] > heap[n]:
            heap[n//2], heap[n] = heap[n], heap[n//2]
        f(n//2)

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    heap = [0] * (N + 1)
    for i in range(N):
        heap[i+1] = nums[i]
        f(i+1)
    last = N
    total = 0
    while last > 0:
        last = last // 2
        total += heap[last]
    print(total)

def enq(n):
    global last
    last += 1
    heap[last] = n
    # 최소힙 유지
    # 부모가 있고, 부모 노드의 데이터가 더 크면 교환
    c = last
    while c//2>0  and heap[c//2] > heap[c]:
        heap[c//2], heap[c] = heap[c], heap[c//2]
        c = c//2

