import sys

sys.stdin = open('max.txt', 'r')


def f(n, k):
    global maxV
    if n == k:
        res = ''.join(map(str, nums))
        if maxV < int(res):
            maxV = int(res)
        return
    else:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                f(n + 1, k)
                nums[j], nums[i] = nums[i], nums[j]

def get_index(m):
    res = 0
    for i in range(len(nums)):
        if nums[i] == m:
            res = i
    return res



T = int(input())
for t in range(1, T +1):
    a, N = input().split()
    nums = list(map(int, list(a)))
    maxV = 0
    N = int(N)
    z = N
    used = [0] * len(a)
    if N > len(nums):
        N = len(nums)
    if N == 1:
        nums[get_index(max(nums))], nums[0] = nums[0], nums[get_index(max(nums))]
        maxV = ''.join(map(str, nums))
    elif z >= 7:
        nums = sorted(nums, reverse=True)
        maxV = ''.join(map(str, nums))
    else:
        f(0, N)
    k = z - len(nums)
    if k % 2 == 0 and k > 0:
        if nums.count(max(nums)) > 1:
            pass
        else:
            temp = list(map(int, list(str(maxV))))
            temp[-1], temp[-2] = temp[-2], temp[-1]
            maxV = ''.join(map(str, temp))
    print(maxV, k)

# 1 321
# 2 7732
# 3 857147
# 4 87664
# 5 88832
# 6 777770
# 7 966354
# 8 954311
# 9 332211
# 10 987645
