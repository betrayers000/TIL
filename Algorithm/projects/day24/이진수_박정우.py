import sys

sys.stdin = open('binary.txt', 'r')

T = int(input())
a = ['A', 'B', 'C', 'D', 'E', 'F']
for t in range(1, T + 1):
    N, nums = input().split()
    N = int(N)
    nums = list(nums)
    for i in range(N):
        if nums[i] in a:
            nums[i] = 10 + a.index(nums[i])
        else:
            nums[i] = int(nums[i])
    result = ''
    for n in nums:
        for j in range(3, -1, -1):
            if n & (1 << j):
                result += '1'
            else:
                result += '0'
    print(f"#{t} {result}")
