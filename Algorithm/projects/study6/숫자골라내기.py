import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    dic = {}
    for i in range(N):
        if dic.get(nums[i]) == None:
            dic[nums[i]] = 1
        else:
            dic[nums[i]] += 1
    before_key = 0
    result = 0
    for key, val in dic.items():
        if val % 2:
            result = result^key
    print(f"Case #{t}")
    print(result)


