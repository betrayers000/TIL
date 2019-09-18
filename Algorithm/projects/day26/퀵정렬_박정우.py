import sys

sys.stdin = open('quick.txt', 'r')

def quick_sort(nlist, p, x):
    if p > x:
        q = partition(nlist, p, x)
        quick_sort(nlist, q-1, x)
        quick_sort(nlist, p, q+1)

def partition(arr, r, x):
    pivot = arr[r]
    for i in range(x, r):
        if pivot > arr[i]:
            arr[i], arr[x] = arr[x], arr[i]
            x += 1
    arr[x], arr[r] = arr[r], arr[x]
    return x

T = int(input())
for t in range(1, T+1):
    N = int(input())
    ilist = list(map(int, input().split()))
    result = [0] * N
    quick_sort(ilist, len(ilist)-1, 0)
    print(ilist[N//2])