import sys

sys.stdin = open('quick.txt', 'r')

def divide(arr, n):
    if len(arr) == 1:
        return arr
    elif arr == []:
        return []
    else:
        left = divide(arr[0:n // 2], len(arr[0:n//2]))
        right = divide(arr[n//2:n], len(arr[n//2:n]))
        return conquer(left, right)

def conquer(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    n, m = len(left) - 1, len(right) - 1
    ni, mi = 0, 0
    ml = [0] * (n + m + 2)
    i = 0
    while i < (n + m + 2):
        if ni > n:
            ml[i] = right[mi]
            mi += 1
        elif mi > m:
            ml[i] = left[ni]
            ni += 1
        elif left[ni] < right[mi]:
            ml[i] = left[ni]
            ni += 1
        else:
            ml[i] = right[mi]
            mi += 1
        i += 1
    return ml


T = int(input())
for t in range(1, T + 1):
    cnt = 0
    N = int(input())
    arr = list(map(int, input().split()))
    s_arr = divide(arr, N)
    print(s_arr[N//2], cnt)
